from Pages.LoginPage import Login

class Engine(Login):
    def __init__(self,page):
        super().__init__(page)

    def click_add_engine_button(self):
        self.page.get_by_role('button',name='添加集群').click()
    def check_popup(self):
        locator=self.locator('el-dialog__header')
        return locator
    # def