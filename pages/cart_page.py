from pages.base_page import BasePage

class CartPage(BasePage):

    CART_LINK = ".nav a[href='/view_cart']"
    REMOVE_BUTTON = ".cart_quantity_delete"

    def open_cart(self):
        self.click(self.CART_LINK)

    def remove_product(self):
        self.page.locator(self.REMOVE_BUTTON).first.click()

    def verify_cart_empty(self):
        return "Cart is empty" in self.page.content()

    VIEW_CART = "text=View Cart"

    def click_view_cart(self):
        self.click(self.VIEW_CART)