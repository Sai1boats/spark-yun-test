import pytest

from Pages.EnginePage import Engine
def test_login():
    p = Engine()
    p.gotos()
    p.inputUser('Sailboats')
    p.inputPassword('welcome1')
    p.click_login_button()
    p.wait(2)
    p.click_addEngine_button()
    p.wait(3)