from pages.home_page import HomePage
from config.config import BASE_URL


def test_verify_home_page_load(page):

    home = HomePage(page)

    home.open_home_page(BASE_URL)

    assert home.verify_home_page_loaded()

PRODUCTS_MENU = "a[href='/products']"

def go_to_products(self):
     self.click(self.PRODUCTS_MENU) 