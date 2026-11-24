from pages.home_page import HomePage
from pages.products_page import ProductsPage
from config.config import BASE_URL

#Category Navigation
def test_category_navigation(page):

    home = HomePage(page)
    products = ProductsPage(page)
    home.open_home_page(BASE_URL)
    products.click_men_category()
    products.click_tshirts_category()
    assert "/category_products/" in page.url

#Brand Navigation
def test_brand_navigation(page):

    home = HomePage(page)
    products = ProductsPage(page)
    home.open_home_page(BASE_URL)
    products.click_polo_brand()
    assert "/brand_products/" in page.url