import re

import allure
import pytest
import yaml
from playwright.sync_api import sync_playwright, expect

from Pages.LoginPage import Login

with open('../test_data.yaml', 'r') as file:
    test_data = yaml.safe_load(file)


@pytest.fixture(scope='module')
def browser_init():
    browser = sync_playwright().start().chromium
    context = browser.launch(headless=False, slow_mo=50).new_context()
    return context


@pytest.fixture(scope='function')
def setup(browser_init):
    page = browser_init.new_page()
    login = Login(page)
    login.goto_homepage(test_data['url'])
    login.wait(1)
    return login


@allure.feature('Login')
class TestLoginPage:

    def test_login_without_content(self, setup):
        self.p = setup
        self.p.wait(3)
        self.p.click_login_button()
        locator1 = self.p.locator_user_filled_prompt()
        locator2 = self.p.locator_password_filled_prompt()
        expect(locator1).to_be_visible()
        expect(locator2).to_be_visible()

    @pytest.mark.parametrize('username,password', [(test_data['admin_user'], test_data['admin_passwd'])])
    def test_login_admin_success(self, setup, username, password):
        self.p = setup
        self.p.inputUser(username)
        self.p.inputPassword(password)
        self.p.click_login_button()
        self.p.wait(1)
        expect(self.p.page).to_have_url(re.compile(".*/home/user-center"))
        self.p.click_logout_button()

    @pytest.mark.parametrize('username,password', [(test_data['test_user'], test_data['test_passwd'])])
    def test_login_user_success(self, setup, username, password):
        self.p = setup
        self.p.inputUser(username)
        self.p.inputPassword(password)
        self.p.click_login_button()
        self.p.wait(1)
        expect(self.p.page).to_have_url(re.compile(".*/home/computer-group"))
        self.p.click_logout_button()

    @pytest.mark.parametrize('username,password', [(test_data['test_user'], test_data['admin_passwd'])])
    def test_login_wrong_password(self, setup, username, password):
        self.p = setup
        self.p.inputUser(username)
        self.p.inputPassword(password)
        self.p.wait(5)
        self.p.click_login_button()
        locator = self.p.locator_wrong_toast()
        expect(locator).to_be_visible(timeout=2000)

    def test_login_wrong_username(self, setup):
        self.p = setup
        self.p.inputUser('toast_test_aaaa')
        self.p.inputPassword('toast_test_bbb')
        self.p.wait(5)
        self.p.click_login_button()
        locator = self.p.locator_wrong_toast()
        expect(locator).to_be_visible(timeout=2000)  # print the context of toast /n print(locator.inner_text())
