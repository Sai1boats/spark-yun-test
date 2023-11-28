from Pages.BasePage import BasePage
from Pages.LoginPage import Login

if __name__ == '__main__':
    p=Login()
    p.gotos()
    p.inputUser('admin')
    p.inputPassword('admin123')
    p.login()