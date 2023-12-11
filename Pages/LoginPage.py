from Pages.BasePage import BasePage


class Login(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def goto_homepage(self, url):
        self.page.goto(url)

    def inputUser(self, user: str):
        self.page.get_by_placeholder('账号/邮箱/手机号').fill(user)

    def inputPassword(self, password: str):
        self.page.get_by_placeholder('密码').fill(password)

    def click_login_button(self):
        self.page.get_by_role("button").click()

    def click_logout_button(self):
        self.page.click('.el-avatar')
        self.page.click('.zqy-home__menu-option:has-text("退出登录")')

    def check_user_filled(self):
        locator = self.page.locator('.el-form-item__error', has_text='请输入账号')
        return locator

    def check_password_filled(self):
        locator = self.page.locator('.el-form-item__error', has_text='请输入密码')
        return locator

    def check_wrong_toast(self):
        locator = self.page.locator('el-message--error')
        return locator
