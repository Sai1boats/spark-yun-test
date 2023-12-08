import pytest

from Pages.LoginPage import Login

def test_login_fail():
    p = Login()
    p.gotos()
    p.inputUser('admin')
    p.inputPassword('admin123')
    p.click_login_button()
    assert '/home/user-center' in p.view_page().url
    p.click_logout_button()
# def test_login_success():
    p.wait(3)
    p.inputUser('Sailboats')
    p.inputPassword('welcome1')
    p.click_login_button()
    assert '/home/computer-group' in p.view_page().url
