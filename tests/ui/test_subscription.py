from pages.home_page import HomePage
from config.config import BASE_URL
from data.test_data import SUBSCRIPTION_EMAIL

def test_verify_subscription(page):

    home = HomePage(page)
    home.open_home_page(BASE_URL)
    home.subscribe(SUBSCRIPTION_EMAIL)
    assert home.verify_subscription_success()