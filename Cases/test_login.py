import re

import allure
import pytest
import yaml
from playwright.sync_api import sync_playwright, expect

from Pages.LoginPage import Login

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
    login = Login(page)
    login.goto_homepage(test_data['url'])
    login.wait(1)
    return login


@allure.feature('Login')
class TestLoginPage:
    @allure.title("测试没有账户密码直接登录提示")
    def test_login_without_content(self, setup):
        self.p = setup
        self.p.wait(3)
        self.p.click_login_button()
        expect(self.p.locator_user_filled_prompt()).to_be_visible()
        expect(self.p.locator_password_filled_prompt()).to_be_visible()

    @allure.title("测试成功登录管理员账号")
    @pytest.mark.parametrize('username,password', [(test_data['admin_user'], test_data['admin_passwd'])])
    def test_login_admin_success(self, setup, username, password):
        self.p = setup
        self.p.input_user(username)
        self.p.input_password(password)
        self.p.click_login_button()
        self.p.wait(1)
        expect(self.p.page).to_have_url(re.compile(".*/home/user-center"))
        self.p.logout()

    @allure.title("测试成功登录普通用户")
    @pytest.mark.parametrize('username,password', [(test_data['test_user'], test_data['test_passwd'])])
    def test_login_user_success(self, setup, username, password):
        self.p = setup
        self.p.input_user(username)
        self.p.input_password(password)
        self.p.click_login_button()
        self.p.wait(1)
        expect(self.p.page).to_have_url(re.compile(".*/home/computer-group"))
        self.p.logout()

    @allure.title("测试错误密码登录账户")
    @pytest.mark.parametrize('username,password', [(test_data['test_user'], test_data['admin_passwd'])])
    def test_login_wrong_password(self, setup, username, password):
        self.p = setup
        self.p.input_user(username)
        self.p.input_password(password)
        self.p.wait(3)
        self.p.click_login_button()
        expect(self.p.locator_wrong_toast()).to_be_visible(timeout=2000)

    @allure.title("测试错误用户名登录账户")
    def test_login_wrong_username(self, setup):
        self.p = setup
        self.p.input_user('toast_test_aaaa')
        self.p.input_password('toast_test_bbb')
        self.p.wait(3)
        self.p.click_login_button()
        expect(self.p.locator_wrong_toast()).to_be_visible(timeout=2000)  # print the context of toast /n print(locator.inner_text())
