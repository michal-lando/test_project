from selenium.webdriver.common.by import By

my_account=(By.CSS_SELECTOR,"div[data-testid='header-adaptive-my-account']")
favorite=(By.CSS_SELECTOR,"div[class='favourites header-ogfstg']")
shopping_box=(By.CSS_SELECTOR,"div[class='MuiBox-root header-wo12yk']")
checkout_button=(By.CSS_SELECTOR,"div[data-testid='header-adaptive-checkout']")
language_button=(By.CSS_SELECTOR,"div[data-testid='header-country-lang-selector']")




class upper_menu:
    def __init__(self, driver):
        self.driver = driver

    def my_account_element(self):
        return self.driver.find_element(my_account[0],my_account[1])

    def favorite_element(self):
        return self.driver.find_element(favorite[0],favorite[1])

    def shopping_box_element(self):
        return self.driver.find_element(shopping_box[0],shopping_box[1])

    def checkout_button_element(self):
        return self.driver.find_element(checkout_button[0],checkout_button[1])

    def language_button_elemet(self):
        return self.driver.find_element(language_button[0],language_button[1])
