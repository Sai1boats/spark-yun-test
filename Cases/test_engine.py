import pytest
import yaml
from playwright.sync_api import sync_playwright, expect

from Pages.EnginePage import Engine

with open('../test_data.yaml', 'r') as file:
    test_data = yaml.safe_load(file)


@pytest.fixture(scope='module')
def browser_init():
    browser = sync_playwright().start().chromium
    context = browser.launch(headless=False, slow_mo=50).new_context()
    return context


@pytest.fixture(scope='function')
def setUp(browser_init):
    page = browser_init.new_page()
    engine = Engine(page)
    engine.goto_homepage(test_data['url'])
    engine.login(test_data['test_user'], test_data['test_passwd'])
    engine.goto_computer_group(test_data['url'])
    return engine


class TestEnginePage:
    def test_show_popup(self, setUp):
        self.p = setUp
        locator_add_engine_button = self.p.locator_add_engine_button()
        expect(locator_add_engine_button).to_be_attached()
        self.p.locator_add_engine_button().click()
        self.p.wait(1)
        add_engine_popup=self.p.locator_add_engine_popup()
        # expect(add_engine_popup).to_be_visible()

