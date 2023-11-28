import sys

from playwright.sync_api import sync_playwright
class BasePage(object):
    @classmethod
    def init_playwright(cls, browser_type: str = "chromium", slow_mos: float = 50.0):
        pw = sync_playwright().start()
        try:
            if browser_type.lower() == 'chromium':
                page =pw.chromium.launch(headless=False, slow_mo=slow_mos).new_page()
            elif browser_type.lower() == 'firefox':
                page=pw.firefox.launch(headless=False, slow_mo=slow_mos).new_page()
            else:
                print("请检查浏览器类型,Windows中支持Chromium或Firefox，Mac中支持Chromium,Firefox或Webkit(暂不支持)")
                sys.exit()
        except Exception as e:
            print("启动浏览器出现错误：", e)
            sys.exit()
        return page
    def __init__(self):
        self.page = self.init_playwright()

    def wait(self,time:float):
        self.page.wait_for_timeout(time*1000)



