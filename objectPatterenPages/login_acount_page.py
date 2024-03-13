from selenium.webdriver.common.by import By

new_customer = (By.CSS_SELECTOR, "div[class='SecondaryContainer']")
register_now =(By.CSS_SELECTOR,"a[href='https://account.next.co.il/en/CustomerRegistration']")
sign_into_title=(By.CSS_SELECTOR,"div[class='SignInTo']")
email=(By.CSS_SELECTOR,"input[name='EmailOrAccountNumber']")
password=(By.CSS_SELECTOR,"input[class='password']")
sign_in=(By.CSS_SELECTOR,"input[id='SignInNow']")
class login_acount_page:
    def __init__(self, driver):
        self.driver = driver

    def new_customer_element(self):
        return self.driver.find_element(new_customer[0],new_customer[1])

    def register_new_element(self):
        return self.driver.find_element(register_now[0],register_now[1])

    def sign_into_title_element(self):
        return self.driver.find_element(sign_into_title[0],sign_into_title[1])

    def email_element(self):
        return self.driver.find_element(email[0],email[1])

    def password_element(self):
        return self.driver.find_element(password[0],password[1])

    def sign_in_element(self):
        return self.driver.find_element(sign_in[0],sign_in[1])

