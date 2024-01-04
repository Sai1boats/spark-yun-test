import allure
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
def setup(browser_init):
    page = browser_init.new_page()
    engine = Engine(page)
    engine.goto_homepage(test_data['url'])
    engine.login(test_data['test_user'], test_data['test_passwd'])
    engine.goto_computer_group(test_data['url'])
    return engine


class TestEnginePage:
    @allure.title("测试添加计算引擎弹窗正常弹出")
    def test_show_popup(self, setup):
        self.p = setup
        expect(self.p.locator_add_engine_button()).to_be_attached()
        self.p.locator_add_engine_button().click()
        self.p.wait(1)
        expect(self.p.locator_add_engine_popup()).to_be_visible()

    @allure.title("添加计算引擎成功")
    @pytest.mark.parametrize('name,types,remark', [('测试计算引擎1', 'yarn', '测试计算引擎1备注')])
    def test_add_engine_success(self, setup, name, types, remark):
        self.p = setup
        self.p.locator_add_engine_button().click()
        self.p.input_name(name)
        self.p.choose_type(types)
        self.p.input_remark(remark)
        self.p.click_confirm()
        self.p.wait(1)
        expect(self.p.locator_added_engine_name()).to_contain_text(name)
        expect(self.p.locator_added_engine_type()).to_contain_text(types)
        expect(self.p.locator_added_engine_remark()).to_contain_text(remark)
