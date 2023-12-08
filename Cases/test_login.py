import pytest
from Pages.LoginPage import Login


class TestLoginPage:
    def test_login_admin(self, before):
        self.p = before
        self.p.inputUser('admin')
        self.p.inputPassword('admin123')
        self.p.click_login_button()
        assert '/home/user-center' in self.p.view_page().url
        self.p.click_logout_button()


    def test_login_success(self,before):
        self.p=before
        self.p.inputUser('Sailboats')
        self.p.inputPassword('welcome1')
        self.p.click_login_button()
        assert '/home/computer-group' in self.p.view_page().url

    def test_login_fail(self,before):
        self.p=before
        self.p.inputUser('Sailboats')
        self.p.inputPassword('welcome')
        self.p.click_login_button()
        assert '/home/computer-group' in self.p.view_page().url

@pytest.fixture(scope='module')
def before():
    page=Login()
    page.goto_homepage()
    yield page
    page.click_logout_button()
    # 不要在 fixture 中改变外部状态
    # p.click_logout_button()
