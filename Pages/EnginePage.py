from Pages.LoginPage import Login


class Engine(Login):
    def __init__(self, page):
        super().__init__(page)

    #页面元素操作
    def locator_add_engine_button(self):
        locator = self.page.locator('xpath=/html/body/div[1]/div/div[2]/div[2]/div[1]/button')
        return locator

    def locator_add_engine_popup(self):
        locator = self.page.locator('xpath=/html/body/div[3]/div/div/header/span')
        return locator
    def locator_added_engine_name(self):
        locator = self.page.locator('xpath=/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span')
        return locator
    def locator_added_engine_type(self):
        locator = self.page.locator('xpath=/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[3]/div/span')
        return locator
    def locator_added_engine_remark(self):
        locator = self.page.locator('xpath=/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[9]/div/span')
        return locator


    #弹窗元素操作
    def input_name(self, strs):
        self.page.locator('xpath=/html/body/div[3]/div/div/div/div/form/div[1]/div/div[1]/div/input').fill(strs)

    def input_remark(self, strs):
        self.page.locator('xpath=/html/body/div[3]/div/div/div/div/form/div[3]/div/div/textarea').fill(strs)

    def choose_type(self, strs):
        self.page.locator('xpath=/html/body/div[3]/div/div/div/div/form/div[2]/div/div/div/div/div/input').click()
        if strs == 'kubernetes':
            self.page.locator('xpath=/html/body/div[2]/div[4]/div/div/div[1]/ul/li[1]').click()
        if strs == 'yarn':
            self.page.locator('xpath=/html/body/div[2]/div[4]/div/div/div[1]/ul/li[2]').click()
        if strs == 'standlone':
            self.page.locator('xpath=/html/body/div[2]/div[4]/div/div/div[1]/ul/li[3]').click()

    def click_confirm(self):
        self.page.locator('xpath=/html/body/div[3]/div/div/footer/button[2]').click()