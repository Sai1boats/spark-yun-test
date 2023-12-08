from Pages.LoginPage import Login

class Engine(Login):
    def __init__(self):
        super().__init__()

    def click_addEngine_button(self):
        self.page.get_by_role('button',name='添加集群')