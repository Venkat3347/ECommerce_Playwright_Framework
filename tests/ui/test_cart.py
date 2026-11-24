from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from config.config import BASE_URL

#Verify Product in Cart
def test_verify_product_in_cart(page):

    home = HomePage(page)
    products = ProductsPage(page)
    cart = CartPage(page)
    home.open_home_page(BASE_URL)
    home.click_products()
    products.add_product_to_cart()
    cart.click_view_cart()
    assert page.locator(".cart_description").is_visible()

#Add Product to Cart
def test_remove_product_from_cart(page):

    home = HomePage(page)
    products = ProductsPage(page)
    cart = CartPage(page)
    home.open_home_page(BASE_URL)
    home.click_products()
    products.add_product_to_cart()
    #cart.add_product_to_cart()
    cart.click_view_cart()
    cart.remove_product()
    assert cart.verify_cart_empty()