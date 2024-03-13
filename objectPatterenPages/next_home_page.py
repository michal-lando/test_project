from selenium.webdriver.common.by import By

site_title=(By.CSS_SELECTOR,"div[class='header-kjwo5n']")
search_box=(By.CSS_SELECTOR,"input[id='header-big-screen-search-box']")
search_button=(By.CSS_SELECTOR,"button[type='submit']")
search_result=(By.CSS_SELECTOR,"h1[data-testid='plp-results-title']")
search_no_result=(By.CSS_SELECTOR,"h1[class='MuiTypography-root MuiTypography-body1 plp-15vemr']")
sign_account=(By.CSS_SELECTOR,"div[class='header-1n6kbbr']")




class next_home_page:
    def __init__(self, driver):
        self.driver = driver
    def find_title(self):
        return self.driver.find_element(site_title[0],site_title[1])

    def find_search_box(self):
        return self.driver.find_element(search_box[0],search_box[1])

    def find_search_button(self):
        return self.driver.find_element(search_button[0],search_button[1])

    def search_result_element(self):
        return self.driver.find_element(search_result[0],search_result[1])

    def search_no_result_element(self):
        return self.driver.find_element(search_no_result[0],search_no_result[1])

    def signin_account_element(self):
        return self.driver.find_element(sign_account[0],sign_account[1])




