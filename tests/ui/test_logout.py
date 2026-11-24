from pages.login_page import LoginPage
from config.config import BASE_URL
from data.test_data import LOGIN_TEST_DATA


def test_logout(page):

    # Get valid login data
    email, password, expected = LOGIN_TEST_DATA[0]
    page.goto(f"{BASE_URL}/login")
    login_page = LoginPage(page)

    # Login
    login_page.login(email, password)

    # Verify login success
    assert login_page.is_login_successful()

    # Logout
    login_page.logout()

    # Verify logout
    assert "/login" in page.url