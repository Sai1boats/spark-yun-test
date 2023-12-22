from playwright.sync_api import Locator

from Pages.BasePage import BasePage


class Login(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def inputUser(self, user: str):
        self.page.get_by_placeholder('账号/邮箱/手机号').fill(user)

    def inputPassword(self, password: str):
        self.page.get_by_placeholder('密码').fill(password)

    def click_login_button(self):
        self.page.get_by_role("button").click()

    def click_logout_button(self):
        self.page.click('.el-avatar')
        self.page.click('.zqy-home__menu-option:has-text("退出登录")')

    def locator_user_filled_prompt(self) -> Locator:
        locator = self.page.locator('xpath=//*[@id="app"]/div/div[2]/div[2]/div/form/div[1]/div/div[2]',
                                    has_text='请输入账号')
        return locator

    def locator_password_filled_prompt(self) -> Locator:
        locator = self.page.locator('xpath=//*[@id="app"]/div/div[2]/div[2]/div/form/div[2]/div/div[2]',
                                    has_text='请输入密码')
        return locator

    def locator_wrong_toast(self) -> Locator:
        locator = self.page.locator('xpath=/html/body/div[4]', has_text='账号或者密码不正确')
        return locator
