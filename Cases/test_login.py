import pytest
from playwright.sync_api import sync_playwright

from Pages.LoginPage import Login
import allure

@pytest.fixture(scope='module')
def browser_init():
    browser=sync_playwright().start().chromium
    context = browser.launch(headless=False, slow_mo=50).new_context()
    return context

@pytest.fixture(scope='function')
def setUp(browser_init):
    page=browser_init.new_page()
    p=Login(page)
    p.goto_homepage('http://127.0.0.1:9998')
    return p

@allure.feature('Login')
class TestLoginPage:
#
    def test_login_without_content(self, setUp):
        self.p = setUp
        self.p.click_login_button()
        locator1= self.p.locator('.el-form-item__error',text='请输入账号')
        assert locator1
        locator2 = self.p.locator('.el-form-item__error', text='请输入密码')
        assert locator2

    def test_login_admin(self, setUp):
        self.p = setUp
        self.p.inputUser('admin')
        self.p.inputPassword('admin123')
        self.p.click_login_button()
        assert '/home/user-center' in self.p.view_page().url
        self.p.click_logout_button()


    def test_login_success(self, setUp):
        self.p=setUp
        self.p.inputUser('Sailboats')
        self.p.inputPassword('welcome1')
        self.p.click_login_button()
        assert '/home/computer-group' in self.p.view_page().url
        self.p.click_logout_button()

    def test_login_wrong(self, setUp):
        self.p=setUp
        self.p.inputUser('Sailboats')
        self.p.inputPassword('welcome')
        self.p.click_login_button()
        locator=self.p.locator('el-message--error')
        assert locator