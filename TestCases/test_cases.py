import time
import pytest
import allure

import objectPatterenPages.register_account as register
from utillities.common_ops import wait, For,get_data
from workflows import flows


search_element = "shoes"
search_no_results = "aa"
user_email ='M0583223614@gmail.com'
user_password ='michal123'
user_name = "Michal"
title_value = "Mrs"
first_name = "Bgtya"
last_name = "miri"
new_email = "bgkul1@mail.com"
new_password = "bmisil1124"
phone = "0504008658"
city = "jerusalem"
appartment = "32"
street = "agasi"
num_house = "7"
# state_value="YERUSHALAYIM"
zipcode = "938765"
invalid_email="michal12"


@pytest.mark.usefixtures('init_webdriver')
class Test_cases:
    @allure.title("test01")
    @allure.description("assert that all elements in upper menu are exists and displayed")
    def test_assert_all_element_in_upper_menu_is_exists(self):
        flows.upper_menu_flows.assert_upper_menu_element_exists()

    @allure.title("test02")
    @allure.description("assert that next logo is show")
    def test_assert_next_site_title(self):
        flows.home_page_flows.assert_page_title_displayed()

    @allure.title("test03")
    @allure.description("assert that you search for product and you have result for that")
    def test_search_product_and_get_results(self):
        flows.home_page_flows.search_product(search_element)
        lower_search = search_element.lower()
        flows.home_page_flows.assert_search_results(lower_search)

    @allure.title("test04")
    @allure.description("assert that you search for prudoct that not exists you get a correct messege")
    def test_search_product_and_no_results(self):
        flows.home_page_flows.search_product(search_no_results)
        flows.home_page_flows.assert_search_no_results()

    @allure.title("test05")
    @allure.description("assert that you are in acounts page")
    def test_assert_insert_into_accounts_page(self):
        flows.login_account_page_flows.login_acount_page()
        flows.login_account_page_flows.assert_login_page()

    @allure.title("test06")
    @allure.description("assert that you get a exception when you type invalid email adress")
    def test_assert_exception_message_when_type_invalid_email(self):
       # flows.login_account_page_flows.login_acount_page()
       flows.login_account_page_flows.login_register_page()
       flows.login_account_page_flows.assert_exception_displayed_invalid_value_in_email(invalid_email)

    @allure.title("test07")
    @allure.description("assert that you could register new user to site")
    def test_assert_new_user_registration(self):
        #use it for run only this test
        #flows.login_account_page_flows.login_acount_page()
        #flows.login_account_page_flows.login_register_page()
        flows.login_account_page_flows.clear_email_field()
        flows.login_account_page_flows.new_user_registration(title_value, first_name, last_name, new_email,
                                                             new_password, phone, city, appartment, street, num_house,
                                                             zipcode)
        wait(For.ELEMENT_DISPLAYED,register.sign_in_acount)
        #time.sleep(5)
        flows.login_account_page_flows.assert_New_user_registration_site(first_name)

    def test_assert_user_acount_in_sign_out_popup(self):
        flows.login_account_page_flows.signout_from_user()
        flows.login_account_page_flows.assert_name_in_popup_is_equals_useraccount()

    @allure.title("test08")
    @allure.description("assert that you could insert with exists user to the account")
    def test_assert_signIn_with_exists_user(self):
       # flows.login_account_page_flows.login_acount_page()
     #   flows.login_account_page_flows.signout_from_user()
        flows.login_account_page_flows.click_on_sign_out_button()
        flows.login_account_page_flows.sign_in_user_exists(user_email, user_password)
        wait(For.ELEMENT_DISPLAYED, register.sign_in_acount)
       # time.sleep(5)
        flows.login_account_page_flows.assert_signin_exists_user(user_name)










