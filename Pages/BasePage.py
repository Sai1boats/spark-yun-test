import os
import time


class BasePage:

    def __init__(self, page):
        self.page = page

    def wait(self, wait_time_by_second: float):
        self.page.wait_for_timeout(wait_time_by_second * 1000)

    # def view_page(self) -> Page:
    #     return self.page

    # def locator(self, selector, text=None, attributes=None) -> Locator:
    #     if text is not None:
    #         return self.page.locator(selector, has_text=text)
    #     elif attributes is not None:
    #         return self.page.locator(selector, has=attributes)
    #     else:
    #         return self.page.locator(selector)

    def screenshots(self, full_page: bool = False, screenshot_dir: str = "../Screenshots",
                    screenshot_name: str = None):
        if screenshot_name is None:
            timestamp = str(time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time())))
            screenshot_name = timestamp + ".jpg"
        screenshot_path = os.path.join(screenshot_dir, screenshot_name)
        self.page.screenshot(full_page=full_page, path=screenshot_path)

    def goto_homepage(self, url:str):
        self.page.goto(url)

    def goto_computer_group(self, url:str):
        self.page.goto(url + "/home/computer-group")

    def goto_datasource(self, url:str):
        self.page.goto(url + "/home/datasource")

    def goto_workflow(self, url:str):
        self.page.goto(url + "/home/workflow")

    def goto_driver_management(self, url:str):
        self.page.goto(url + "/home/driver-management")

    def goto_schedule(self, url:str):
        self.page.goto(url + "/home/scheduler")

    def goto_tenant_user(self, url:str):
        self.page.goto(url + "/home/tenant-user")

    def login(self, username: str, password: str):
        self.page.get_by_placeholder('账号/邮箱/手机号').fill(username)
        self.page.get_by_placeholder('密码').fill(password)
        self.page.get_by_role("button").click()
