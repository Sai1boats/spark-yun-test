import allure
import pytest
from playwright.sync_api import sync_playwright

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
        self.p.click_login_button()
        locator1 = self.p.check_user_filled_prompt()
        assert locator1
        locator2 = self.p.check_password_filled_prompt()
        assert locator2

    def test_login_admin_success(self, setup):
        self.p = setup
        self.p.inputUser('admin')
        self.p.inputPassword('admin123')
        self.p.click_login_button()
        self.p.wait(1)
        assert '/home/user-center' in self.p.view_page().url
        self.p.click_logout_button()

    def test_login_user_success(self, setup):
        self.p = setup
        self.p.inputUser('Sailboats')
        self.p.inputPassword('welcome1')
        self.p.click_login_button()
        self.p.wait(1)
        assert '/home/computer-group' in self.p.view_page().url
        self.p.click_logout_button()

    def test_login_wrong_password(self, setup):
        self.p = setup
        self.p.inputUser('Sailboats')
        self.p.inputPassword('welcome')
        self.p.click_login_button()
        locator = self.p.check_wrong_toast()
        assert locator

    def test_login_wrong_username(self, setup):
        self.p = setup
        self.p.inputUser('test')
        self.p.inputPassword('test')
        self.p.click_login_button()
        locator = self.p.check_wrong_toast()
        assert locator

