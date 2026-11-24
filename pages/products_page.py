from pages.base_page import BasePage

class ProductsPage(BasePage):

    SEARCH_BOX = "#search_product"
    SEARCH_BUTTON = "#submit_search"
    SEARCHED_PRODUCTS = ".features_items"
    VIEW_FIRST_PRODUCT = "a[href='/product_details/1']"
    ADD_FIRST_PRODUCT = "a[data-product-id='1']"
    CONTINUE_SHOPPING = "button:has-text('Continue Shopping')"
    MEN_CATEGORY = "a[href='#Men']"
    MEN_TSHIRTS = "a[href='/category_products/3']"
    POLO_BRAND = "a[href='/brand_products/Polo']"
    PRODUCT_ADDED_MESSAGE = "text=Your product has been added to cart."

    def search_product(self, product_name):
        self.fill(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)

    def verify_search_results(self):
        return self.is_visible(self.SEARCHED_PRODUCTS)

    def view_product(self):
        self.click(self.VIEW_FIRST_PRODUCT)

    def verify_product_details_page(self):
        return "/product_details/" in self.page.url

    def add_product_to_cart(self):
        #self.page.locator(".product-image-wrapper").first.hover()
        self.page.locator(self.ADD_FIRST_PRODUCT).first.click()

    def click_men_category(self):
        self.click(self.MEN_CATEGORY)

    def click_tshirts_category(self):
        self.click(self.MEN_TSHIRTS)

    def click_polo_brand(self):
        self.click(self.POLO_BRAND)

    def verify_product_added(self):
        self.page.wait_for_timeout(2000)
        return self.is_visible(self.PRODUCT_ADDED_MESSAGE)

    VIEW_CART = "text=View Cart"
    
    def click_view_cart(self):
        self.click(self.VIEW_CART)