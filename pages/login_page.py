from pages.base_page import BasePage

class LoginPage(BasePage):

    # Logout locators
    LOGIN_EMAIL = "[data-qa='login-email']"
    LOGIN_PASSWORD = "[data-qa='login-password']"
    LOGIN_BUTTON = "[data-qa='login-button']"

    # Logout locators
    LOGOUT_BUTTON = "a[href='/logout']"
    LOGIN_TO_ACCOUNT_TEXT = "text=Login to your account"
    
    SUCCESS_LOGIN = "text=Logged in as"
    INVALID_LOGIN = "text=Your email or password is incorrect!"

    def login(self, email, password):
        self.fill(self.LOGIN_EMAIL, email)
        self.fill(self.LOGIN_PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def is_login_successful(self):
        return self.is_visible(self.SUCCESS_LOGIN)

    def is_login_failed(self):
        return self.is_visible(self.INVALID_LOGIN)
    
    def logout(self):
        self.click(self.LOGOUT_BUTTON)

    def is_logout_succesfull(self):
        return self.is_visible(self.LOGIN_TO_ACCOUNT_TEXT)