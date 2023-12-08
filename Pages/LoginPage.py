from Pages.BasePage import BasePage


class Login(BasePage):
    def __init__(self):
        super().__init__()
    def goto_homepage(self):
        self.page.goto('http://127.0.0.1:9998')

    def inputUser(self,user:str):
        self.page.get_by_placeholder('账号/邮箱/手机号').fill(user)

    def inputPassword(self,password:str):
        self.page.get_by_placeholder('密码').fill(password)

    def click_login_button(self):
        self.page.get_by_role("button").click()

    def click_logout_button(self):
        self.page.click('.el-avatar')
        self.page.click('.zqy-home__menu-option:has-text("退出登录")')

