import re

import allure
import pytest
from playwright.sync_api import sync_playwright, expect

from Pages.LoginPage import Login


@pytest.fixture(scope='module')
def browser_init():
    browser = sync_playwright().start().chromium
    context = browser.launch(headless=False, slow_mo=50).new_context()
    return context


@pytest.fixture(scope='function')
def setup(browser_init):
    page = browser_init.new_page()
    p = Login(page)
    p.goto_homepage('http://127.0.0.1:9998')
    p.wait(1)
    return p


@allure.feature('Login')
class TestLoginPage:
    #
    def test_login_without_content(self, setup):
        self.p = setup
        self.p.wait(3)
        self.p.click_login_button()
        locator1 = self.p.check_user_filled_prompt()
        locator2 = self.p.check_password_filled_prompt()
        expect(locator1).to_be_visible()
        expect(locator2).to_be_visible()
        self.p.screenshots()

    def test_login_admin_success(self, setup):
        self.p = setup
        self.p.inputUser('admin')
        self.p.inputPassword('admin123')
        self.p.click_login_button()
        self.p.wait(1)
        expect(self.p.page).to_have_url(re.compile(".*/home/user-center"))
        self.p.click_logout_button()

    def test_login_user_success(self, setup):
        self.p = setup
        self.p.inputUser('Sailboats')
        self.p.inputPassword('welcome1')
        self.p.click_login_button()
        self.p.wait(1)
        expect(self.p.page).to_have_url(re.compile(".*/home/computer-group"))
        self.p.click_logout_button()

    def test_login_wrong_password(self, setup):
        self.p = setup
        self.p.inputUser('Sailboats')
        self.p.inputPassword('welcome')
        self.p.wait(5)
        self.p.click_login_button()
        locator = self.p.check_wrong_toast()
        expect(locator).to_be_visible(timeout=2000)

    def test_login_wrong_username(self, setup):
        self.p = setup
        self.p.inputUser('no_toast')
        self.p.inputPassword('no_toast')
        self.p.wait(5)
        self.p.click_login_button()
        locator = self.p.check_wrong_toast()
        expect(locator).to_be_visible(timeout=2000)
        # print the context of toast
        # print(locator.inner_text())
