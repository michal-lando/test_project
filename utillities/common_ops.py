import csv
import xml.etree.ElementTree as ET
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import TestCases.conftest as conf

def wait(for_element,element):
    if for_element=='element_exists':
        WebDriverWait(conf.driver,5).until(EC.presence_of_element_located((element[0],element[1])))

    elif for_element=='element_displayed':
        WebDriverWait(conf.driver,5).until(EC.visibility_of_element_located((element[0],element[1])))

#Enum FOR SELECTING DISPLAYED ELEMENT
class For:
    ELEMENT_EXISTS='element_exists'
    ELEMENT_DISPLAYED='element_displayed'

#def read_csv(file_name):
#    data = []
#    with open(file_name, newline='') as file:
#        reader = csv.reader(file)
#        for row in reader:
#            data.insert(len(data), row)
#        return data

def get_data(node_name):
    root = ET.parse("C:/Users/מיכל/test_project/external_files/data.xml").getroot()
    return root.find('.//' + node_name).text

