from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class verification:
    def verify_equals(actual_result, expected_result):
        assert str(actual_result) == str(expected_result), "the actual result: " + str(
            actual_result) + " not as the expected result: " + expected_result


    def verify_element_Displayed(displayed_element: WebElement):
        assert displayed_element.is_displayed(),"the element not displayed"


    def verify_element_not_displayed(not_displayed_element: WebElement):
        assert not not_displayed_element.is_displayed(),"the element do not displayed"


    def verify_not_equals(actual_result, value):
        assert not str(actual_result) == str(value), " not corect the actual result: " + str(
            actual_result) + " equals to: "+str(value)

    def verify_text_exists_in_element(value,element_text):
        assert value in element_text,"the text is not exists in"+element_text.text

    #verify menu button with smart assert

    @staticmethod
    def soft_assert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()


    #verify menu button with smart dispalyed

    def soft_displayed(elem_list):
        failed_elems=[]
        for i in range(len(elem_list)):
            if not elem_list[i].is_displayed():
                failed_elems.insert(len(failed_elems),elem_list[i].get_attribute('value'))
        if len(failed_elems)>0:
            for x in failed_elems:
                print(" element not displayed: "+ str(x))
            raise AssertionError('soft displayed failed')


    def verify_num_of_element(elems,count):
        assert len(elems)==count, 'num of element in list: '+str(len(elems))+ ' doesnt match expected: ' +str(count)



