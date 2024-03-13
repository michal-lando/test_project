from selenium.webdriver.common.by import By

title = (By.CSS_SELECTOR, "select[name='Title']")
first_name= (By.CSS_SELECTOR, "input[name='FirstName']")
last_name= (By.CSS_SELECTOR, "input[name='LastName']")
email= (By.CSS_SELECTOR, "input[name='Email']")
phone= (By.CSS_SELECTOR, "input[id='PhoneNumber']")
password=(By.CSS_SELECTOR,"input[name='Password']")
apartment= (By.CSS_SELECTOR, "input[id='AddressLine1']")
city=(By.CSS_SELECTOR, "input[id='AddressLine4']")
street_num=(By.CSS_SELECTOR, "input[id='AddressLine2']")
state=(By.CSS_SELECTOR, "input[id='AddressLine6']")
zip_code=(By.CSS_SELECTOR, "input[id='AddressLine6']")
check_email=(By.CSS_SELECTOR,"input[name='ChkByEmail']")
sales_emails=(By.CSS_SELECTOR,"input[id='ChkBySale']")
check_sms=(By.CSS_SELECTOR,"input[name='ChkBySms']")
sign_up_button=(By.CSS_SELECTOR,"button[id='SignupButton']")
sign_in_acount=(By.CSS_SELECTOR,"span[data-testid='header-myaccount-username']")
sign_out_popup=(By.CSS_SELECTOR,"div[class='header-10my9lm']")
sign_out_button=(By.CSS_SELECTOR,"div[class='header-1xfwofk']")
sign_out_account=(By.CSS_SELECTOR,"span[data-testid='header-my-account-container-tooltip-username']")
invalid_exception_email=(By.CSS_SELECTOR,"span[id='Email-error']")




class register_account_page:
    def __init__(self, driver):
        self.driver = driver

    def title_element(self):
        return self.driver.find_element(title[0], title[1])

    def first_name_element(self):
        return self.driver.find_element(first_name[0], first_name[1])

    def last_name_element(self):
        return self.driver.find_element(last_name[0], last_name[1])

    def email_element(self):
        return self.driver.find_element(email[0], email[1])

    def phone_element(self):
        return self.driver.find_element(phone[0], phone[1])

    def password_element(self):
        return self.driver.find_element(password[0], password[1])

    def appartment_element(self):
        return self.driver.find_element(apartment[0],apartment[1])

    def street_num_element(self):
        return self.driver.find_element(street_num[0],street_num[1])

    def city_element(self):
        return self.driver.find_element(city[0], city[1])

    def state_element(self):
        return self.driver.find_element(state[0],state[1])

    def zip_code_element(self):
        return self.driver.find_element(zip_code[0],zip_code[1])

    def check_email_element(self):
        return self.driver.find_element(check_email[0], check_email[1])

    def check_sms_element(self):
        return self.driver.find_element(check_sms[0], check_sms[1])

    def check_email_sales_element(self):
        return self.driver.find_element(sales_emails[0],sales_emails[1])

    def sign_up_button_element(self):
        return self.driver.find_element(sign_up_button[0], sign_up_button[1])

    def sign_in_acount_element(self):
        return self.driver.find_element(sign_in_acount[0], sign_in_acount[1])

    def invalid_exception_email(self):
        return self.driver.find_element(invalid_exception_email[0],invalid_exception_email[1])

    def sign_out_element(self):
        return self.driver.find_element(sign_out_button[0],sign_out_button[1])

    def sign_out_popup_element(self):
        return self.driver.find_element(sign_out_popup[0],sign_out_popup[1])

    def sign_out_acount_alament(self):
        return self.driver.find_element(sign_out_account[0],sign_out_account[1])


