from Pages.BasePage import BasePage


class Login(BasePage):
    def __init__(self):
        super().__init__()
    def gotos(self):
        self.page.goto('http://127.0.0.1:9998')

    def inputUser(self,user:str):
        self.page.get_by_placeholder('账号/邮箱/手机号').fill(user)

    def inputPassword(self,password:str):
        self.page.get_by_placeholder('密码').fill(password)

    def login(self):
        self.page.get_by_role("button").click()

