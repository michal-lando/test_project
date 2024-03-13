import TestCases.conftest
from objectPatterenPages.login_acount_page import login_acount_page
from objectPatterenPages.next_home_page import next_home_page
from objectPatterenPages.upper_menu import upper_menu
from objectPatterenPages.register_account import register_account_page

web_loginAccount=None
web_nextHome=None
web_upperMenu=None
web_registerAccount=None

class managePages:
    @staticmethod
    def init_web_pages():
        globals()['web_loginAccount']=login_acount_page(TestCases.conftest.driver)
        globals()['web_nextHome'] = next_home_page(TestCases.conftest.driver)
        globals()['web_upperMenu'] = upper_menu(TestCases.conftest.driver)
        globals()['web_registerAccount']=register_account_page(TestCases.conftest.driver)

