import re

import allure
import pytest
import yaml
from playwright.sync_api import sync_playwright, expect

from Pages.AdminPage import AdminPage

with open('../test_data.yaml', 'r') as file:
    test_data = yaml.safe_load(file)


@pytest.fixture(scope='class')
def browser_init():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture(scope='function')
def setup(browser_init):
    page = browser_init.new_page()
    admin = AdminPage(page)
    admin.goto_homepage(test_data['url'])
    admin.input_user(test_data['admin_user'])
    admin.input_password(test_data['admin_passwd'])
    admin.click_login_button()
    yield admin


@allure.feature('测试后台管理部分')
class TestAdminPage:
    @allure.title("测试成功登录管理员账号")
    @pytest.mark.parametrize('username,password', [(test_data['admin_user'], test_data['admin_passwd'])])
    def test_login_admin_success(self, setup, username, password):
        self.p = setup
        expect(self.p.page).to_have_url(re.compile(".*/home/user-center"))
        self.p.logout()

    @allure.title("测试创建账户成功")
    @pytest.mark.parametrize('name,account,password,phone,email,remark',
                             [('tester', 'testers', 'welcome1', '18888888888', 'test@em.com', '备注')])
    def test_create_account_success(self, setup, name, account, password, phone, email, remark):
        self.p = setup
        self.p.locator_add_user_button().click()
        expect(self.p.locator_add_user_popup()).to_be_visible()
        self.p.locator_add_user_name().fill(name)
        self.p.locator_add_user_account().fill(account)
        self.p.locator_add_user_password().fill(password)
        self.p.locator_add_user_phone().fill(phone)
        self.p.locator_add_user_email().fill(email)
        self.p.locator_add_user_remark().fill(remark)
        self.p.locator_add_user_confirm().click()
        self.p.wait(1)
        expect(self.p.locator_user_name()).to_contain_text(name)
        expect(self.p.locator_user_email()).to_contain_text(email)
        expect(self.p.locator_user_account()).to_contain_text(account)
        expect(self.p.locator_user_phone()).to_contain_text(phone)
        expect(self.p.locator_user_remark()).to_contain_text(remark)
        expect(self.p.locator_user_status()).to_contain_text('启用')

    @allure.title("测试创建账户失败-账户重复")
    @pytest.mark.parametrize('name,password,phone,email,remark',
                             [('tester1',  'welcome1', '18888888888', 'test@em.com', '备注')])
    def test_create_account_duplication(self, setup, name, password, phone, email, remark):
        self.p = setup
        expect(self.p.locator_user_account()).to_be_visible()
        account=self.p.locator_user_account().inner_text()
        self.p.locator_add_user_button().click()
        expect(self.p.locator_add_user_popup()).to_be_visible()
        self.p.locator_add_user_name().fill(name)
        self.p.locator_add_user_account().fill(account)
        self.p.locator_add_user_password().fill(password)
        self.p.locator_add_user_phone().fill(phone)
        self.p.locator_add_user_email().fill(email)
        self.p.locator_add_user_remark().fill(remark)
        self.p.locator_add_user_confirm().click()
        self.p.wait(1)
        expect(self.p.locator_user_duplication_toast()).to_be_visible()
        expect(self.p.locator_user_duplication_toast()).to_contain_text('用户已存在')

    # @allure.title("测试创建账户失败-账户重复")
    # @pytest.mark.parametrize('name,password,phone,email,remark',
    #                          [('tester1',  'welcome1', '18888888888', 'test@em.com', '备注')])
    # def test_create_account_duplication(self, setup, name, password, phone, email, remark):
    #     self.p = setup
    #     expect(self.p.locator_user_account()).to_be_visible()
    #     account=self.p.locator_user_account().inner_text()
    #     self.p.locator_add_user_button().click()
    #     expect(self.p.locator_add_user_popup()).to_be_visible()
    #     self.p.locator_add_user_name().fill(name)
    #     self.p.locator_add_user_account().fill(account)
    #     self.p.locator_add_user_password().fill(password)
    #     self.p.locator_add_user_phone().fill(phone)
    #     self.p.locator_add_user_email().fill(email)
    #     self.p.locator_add_user_remark().fill(remark)
    #     self.p.locator_add_user_confirm().click()
    #     self.p.wait(1)
    #     expect(self.p.locator_user_duplication_toast()).to_be_visible()
    #     expect(self.p.locator_user_duplication_toast()).to_contain_text('用户已存在')
