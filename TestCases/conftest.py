import time
import pytest
import selenium
import selenium.webdriver
import selenium.webdriver.chrome.webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utillities.common_ops import get_data
from utillities.manage_pages import managePages
# הגדרת משתנים מסוג דרייבר ואחרד מסוג ווב דרייבר שיכיל את שם הדפדפן
driver = None
action = None
web_driver ='edge'

@pytest.fixture(scope='class')
def init_webdriver(request):
    global action
    globals()['driver'] = get_web_driver()
    driver = globals()['driver']
    driver.maximize_window()
    time.sleep(5)
    driver.get('https://www.next.co.il/en')
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    managePages.init_web_pages()
    # מבצע את ההפעולה של סגירת הדפדפן לאחר הסיום
    yield
    driver.quit()

def get_chrome():
    # פונקצייה המחזירה דפדפן מסוג כרום
    chrome_driver = selenium.webdriver.Chrome(ChromeDriverManager().install())
    return chrome_driver


def get_firefox():
    # פונקצייה המחזירה פונקצייה מסוג פיירפוקס
    firefox_driver = selenium.webdriver.Firefox(GeckoDriverManager().install())
    return firefox_driver


def get_edge():
    # פונקצייה המחזירה פונקציה מסוג אדג'
    edge_driver = selenium.webdriver.Edge(EdgeChromiumDriverManager().install())
    return edge_driver


def get_web_driver():
    # פונקציה הבוחרת את הדרייבר המתאים לפי הערך שנשלח מהמשתמש עבור הבדיקות
    if web_driver.lower() == 'chrome':
        driver = get_chrome()
    elif web_driver.lower() == 'edge':
        driver = get_edge()
    elif web_driver.lower() == 'firefox':
        driver = get_firefox()
    else:
        driver = None
        raise Exception("wrong driver name")
    return driver

