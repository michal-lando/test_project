import time
import allure
from extensions.actions import actions
from extensions.verification import verification
from utillities import manage_pages as mng

class home_page_flows:
    @staticmethod
    def assert_page_title_displayed():
        verification.verify_element_Displayed(mng.web_nextHome.find_title())

    @staticmethod
    def search_product(product_name):
        actions.sendkeys_action(mng.web_nextHome.find_search_box(),product_name)
        actions.click_action(mng.web_nextHome.find_search_button())

    @staticmethod
    def assert_search_results(search_product):
        result=(mng.web_nextHome.search_result_element().text).lower()
        title_result=result.strip().replace('"', '')
        verification.verify_equals(search_product,title_result)

    @staticmethod
    def assert_search_no_results():
        verification.verify_element_Displayed(mng.web_nextHome.search_no_result_element())


class login_account_page_flows:
    @staticmethod
    def login_acount_page():
        actions.click_action(mng.web_nextHome.signin_account_element())

    @staticmethod
    def assert_login_page():
        verification.verify_element_Displayed(mng.web_loginAccount.new_customer_element())

    @staticmethod
    def login_register_page():
        actions.click_action(mng.web_loginAccount.register_new_element())

    @staticmethod
    def sign_in_user_exists(exists_email, exists_password):
        actions.sendkeys_action(mng.web_loginAccount.email_element(),exists_email)
        actions.sendkeys_action(mng.web_loginAccount.password_element(),exists_password)
        actions.click_action(mng.web_loginAccount.sign_in_element())

    @staticmethod
    def assert_signin_exists_user(user_name):
        verification.verify_equals(user_name,mng.web_loginAccount.sign_into_title_element())

    @staticmethod
    def new_user_registration(title_value,n_firstName,n_lastName,n_email,n_password,n_phone,n_city,n_appartment,n_street,n_num_house,n_zipcode):
        actions.select_by_value(mng.web_registerAccount.title_element(),title_value)
        actions.sendkeys_action(mng.web_registerAccount.first_name_element(),n_firstName)
        actions.sendkeys_action(mng.web_registerAccount.last_name_element(),n_lastName)
        actions.sendkeys_action(mng.web_registerAccount.email_element(),n_email)
        actions.sendkeys_action(mng.web_registerAccount.phone_element(),n_phone)
        actions.sendkeys_action(mng.web_registerAccount.password_element(),n_password)
        actions.sendkeys_action(mng.web_registerAccount.appartment_element(),n_appartment)
        actions.sendkeys_action(mng.web_registerAccount.street_num_element(),n_num_house+" "+n_street)
        actions.sendkeys_action(mng.web_registerAccount.city_element(),n_city)
     #   actions.select_by_value(mng.web_registerAccount.state_element(),n_state_value)
        actions.sendkeys_action(mng.web_registerAccount.zip_code_element(),n_zipcode)
        actions.click_action(mng.web_registerAccount.check_email_element())
        actions.click_action(mng.web_registerAccount.check_email_sales_element())
        actions.click_action(mng.web_registerAccount.sign_up_button_element())

    @staticmethod
    def assert_New_user_registration_site(expected_account_name):
        actual_account_name=actions.element_text(mng.web_registerAccount.sign_in_acount_element())
     #   actual_account_name=mng.web_registerAccount.sign_in_acount_element().text
        verification.verify_equals(actual_account_name,expected_account_name)

    @staticmethod
    def assert_exception_displayed_invalid_value_in_email(invalid_email):
        actions.sendkeys_action(mng.web_registerAccount.email_element(),invalid_email)
        actions.click_action(mng.web_registerAccount.password_element())
        verification.verify_element_Displayed(mng.web_registerAccount.invalid_exception_email())

    @staticmethod
    def assert_exception_invalid_email_not_displayed():
        verification.verify_element_not_displayed(mng.web_registerAccount.invalid_exception_email())

    @staticmethod
    def clear_email_field():
        actions.clear_action(mng.web_registerAccount.email_element())

    @staticmethod
    def insert_value_in_email(n_email):
        actions.sendkeys_action(mng.web_registerAccount.email_element(),n_email)

    @staticmethod
    def signout_from_user():
        actions.click_action(mng.web_registerAccount.sign_in_acount_element())

    @staticmethod
    def click_on_sign_out_button():
        actions.click_action(mng.web_registerAccount.sign_out_element())

    @staticmethod
    def assert_popup_sign_out_displayed():
        verification.verify_element_Displayed(mng.web_registerAccount.sign_out_popup_element())

    @staticmethod
    def assert_name_in_popup_is_equals_useraccount():
        user_account=actions.element_text(mng.web_registerAccount.sign_in_acount_element())
        user_in_sign_out=actions.element_text(mng.web_registerAccount.sign_in_acount_element())
        verification.verify_text_exists_in_element(user_account,user_in_sign_out)



class upper_menu_flows:
    @staticmethod
    def assert_upper_menu_element_exists():
        upper_menu_elements = [mng.web_upperMenu.my_account_element(),
                 mng.web_upperMenu.favorite_element(),
                 mng.web_upperMenu.shopping_box_element(),
                 mng.web_upperMenu.shopping_box_element(),
                 mng.web_upperMenu.language_button_elemet()]
        verification.soft_assert(upper_menu_elements)






