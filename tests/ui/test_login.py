import pytest

from pages.login_page import LoginPage
from config.config import BASE_URL
from data.test_data import LOGIN_TEST_DATA

@pytest.mark.parametrize("email,password,expected",LOGIN_TEST_DATA)
def test_login(page,email,password,expected):

    page.goto(f"{BASE_URL}/login")
    login_page = LoginPage(page)
    login_page.login(email,password)

    if expected == "success":
       assert login_page.is_login_successful()

    elif expected == "failure":
        assert login_page.is_login_failed()