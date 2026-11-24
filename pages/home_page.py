from pages.base_page import BasePage

class HomePage(BasePage):

    LOGO = "img[alt='Website for automation practice']"
    SIGNUP_LOGIN_LINK = "a[href='/login']"
    SUBSCRIPTION_EMAIL = "#susbscribe_email"
    SUBSCRIBE_BUTTON = "#subscribe"
    SUCCESS_MESSAGE = "text=You have been successfully subscribed!"

    

    def open_home_page(self, url):
        self.navigate(url)

    def verify_home_page_loaded(self):
        self.wait_for_element(self.LOGO)

        return self.is_visible(self.LOGO)
    
    def click_signup_login(self):
        self.click(self.SIGNUP_LOGIN_LINK)

    PRODUCTS_LINK = "a[href='/products']"

    def click_products(self):
        self.click(self.PRODUCTS_LINK)

    def subscribe(self, email):
         self.page.locator(self.SUBSCRIPTION_EMAIL).scroll_into_view_if_needed()
         self.fill(self.SUBSCRIPTION_EMAIL, email)
         self.click(self.SUBSCRIBE_BUTTON)

    def verify_subscription_success(self):
         self.wait_for_element(self.SUCCESS_MESSAGE)
         return self.is_visible(self.SUCCESS_MESSAGE)