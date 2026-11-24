from pages.home_page import HomePage
from pages.signup_page import SignupPage
from config.config import BASE_URL
from data.test_data import get_test_user

def test_verify_account_creation(page):
    TEST_USER= get_test_user()
    home = HomePage(page)
    signup = SignupPage(page)
    home.open_home_page(BASE_URL)
    home.click_signup_login()
    signup.signup_user(TEST_USER["name"],TEST_USER["email"])
    signup.fill_account_details(TEST_USER)
    signup.create_account()
def verify_account_created(self):

    expected_text = "ACCOUNT CREATED!"
    actual_text = self.get_text(self.ACCOUNT_CREATED).strip()
  
    return expected_text == actual_text
    # assert signup.verify_account_created()