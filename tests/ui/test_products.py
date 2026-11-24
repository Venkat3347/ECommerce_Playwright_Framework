from pages.home_page import HomePage
from pages.products_page import ProductsPage
from config.config import BASE_URL

#Navigate to Products
def test_navigate_to_products(page):

    home = HomePage(page)
    home.open_home_page(BASE_URL)
    home.click_products()
    assert "/products" in page.url

#Search products
def test_search_product(page):

    home = HomePage(page)
    products = ProductsPage(page)
    home.open_home_page(BASE_URL)
    home.click_products()
    products.search_product("Blue Top")
    assert products.verify_search_results()

#View Product Details
def test_view_product_details(page):

    home = HomePage(page)
    products = ProductsPage(page)
    home.open_home_page(BASE_URL)
    home.click_products()
    products.view_product()
    assert products.verify_product_details_page()

#Add Product to Cart
def test_add_product_to_cart(page):

    home = HomePage(page)
    products = ProductsPage(page)
    home.open_home_page(BASE_URL)
    home.click_products()
    products.add_product_to_cart()
    assert products.verify_product_added()