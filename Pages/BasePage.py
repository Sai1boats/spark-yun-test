class BasePage:

    def __init__(self, page):
        self.page = page

    def wait(self, time: float):
        self.page.wait_for_timeout(time * 1000)

    def view_page(self):
        return self.page

    def locator(self, selector, text=None, attributes=None):
        if text is not None:
            return self.page.locator(selector, has_text=text)
        elif attributes is not None:
            return self.page.locator(selector, has=attributes)
        else:
            return self.page.locator(selector)

    def screenshot(self):
        self.screenshot()