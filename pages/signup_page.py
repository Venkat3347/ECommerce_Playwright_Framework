from pages.base_page import BasePage

class SignupPage(BasePage):

    NAME = "input[data-qa='signup-name']"
    EMAIL = "input[data-qa='signup-email']"
    SIGNUP_BTN = "button[data-qa='signup-button']"
    ACCOUNT_CREATED = "h2[data-qa='account-created']"
    ENTER_ACCOUNT_INFORMATION = "b:has-text('Enter Account Information')"

    PASSWORD = "#password"

    FIRST_NAME = "#first_name"
    LAST_NAME = "#last_name"

    COMPANY = "#company"

    ADDRESS = "#address1"

    ADDRESS2 = "#address2"

    COUNTRY = "#country"

    STATE = "#state"

    CITY = "#city"

    ZIPCODE = "#zipcode"

    MOBILE = "#mobile_number"

    CREATE_ACCOUNT = \
        "button[data-qa='create-account']"

    ACCOUNT_CREATED = \
        "h2[data-qa='account-created']"

    def signup_user(self, name, email):

        self.fill(self.NAME, name)

        self.fill(self.EMAIL, email)

        self.click(self.SIGNUP_BTN)

    def fill_account_details(self, user):

        self.fill(self.PASSWORD,user["password"])

        self.fill(self.FIRST_NAME,user["first_name"])

        self.fill(self.LAST_NAME,user["last_name"])

        self.fill(self.COMPANY,user["company"])

        self.fill(self.ADDRESS,user["address"])

        self.fill(self.ADDRESS2,user["address2"])

        self.page.select_option(self.COUNTRY, user["country"])

        self.fill(self.STATE,user["state"])

        self.fill(self.CITY,user["city"])

        self.fill(self.ZIPCODE,user["zipcode"])

        self.fill(self.MOBILE,user["mobile"])

    def create_account(self):
        self.click(self.CREATE_ACCOUNT )

    def account_created(self):
        return self.is_visible(self.ACCOUNT_CREATED)

    def verify_account_created(self):
        expected_text = "ACCOUNT CREATED!"
        actual_text = self.get_text(self.ACCOUNT_CREATED)
        return expected_text == actual_text
    def verify_enter_account_information(self):
        return self.is_visible(self.ENTER_ACCOUNT_INFORMATION)