
from Pages.LoginPage import Login

def test_login():
    p = Login()
    p.gotos()
    p.inputUser('admin')
    p.inputPassword('admin123')
    p.login()