from Pages.LoginPage import Login


class Engine(Login):
    def __init__(self, page):
        super().__init__(page)

    def locator_add_engine_button(self):
        locator = self.page.locator('xpath=/html/body/div[1]/div/div[2]/div[2]/div[1]/button')
        return locator

    def locator_add_engine_popup(self):
        locator = self.page.locator('xpath=/html/body/div[4]/div/div/div')
        return locator
