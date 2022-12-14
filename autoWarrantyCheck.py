'''
This python file run the automated testing for warranty checking.
"selenium 4.3.0" and correct ver webdriver is needing for running the test. 
'''

import sys
import json
import string
import random
import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import noElementException
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.safari.service import Service as safariService

import element
def logPassword(password, filename):
            f = open(filename, "a")
            f.write("{0} -- {1}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), password))
            f.close()
            
def randomSymGenerate(size:int)->str:
            #Generate random characters for testing
            #para size: int, length of string
            special = string.punctuation
            specialSym = random.sample(special,size)
            random.shuffle(specialSym)
            return ''.join(specialSym)
    
def randomStrGenerate(size:int)->str:
            #Generate random characters
            #para size: int, length of string
            return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        
class warrantyCheck():
    
        def testValidWarranty():
            jsonFilePath = "ValidSerial.json"
            f = open(jsonFilePath)
            data = json.load(f)
            f.close()
            for key, val in data.items():
                textarea.click()
                textarea.clear()
                textarea.send_keys(val)
                textarea.send_keys(Keys.ENTER)
                driver.implicitly_wait(20)
                serialNumberFound = True
                try:
                    rstItem = driver.find_element("class name",element.RST_ITEM)
                except noElementException:
                    serialNumberFound = False
                    
                if serialNumberFound == True:
                    result = logPassword(f"testValidWarranty phase : Warranty {val} found",filename)
                else:
                    result = logPassword(f"testValidWarranty phase : Warranty {val} not found",filename)
                    
            return result
    
        def testInvalidWarranty():
            textarea.click()
            textarea.clear()
            input = randomSymGenerate(6)
            textarea.send_keys(input)
            textarea.send_keys(Keys.ENTER)
            sleep(1)
            spans = driver.find_elements("class name",element.SPAN)
            
            if spans[0].get_attribute("style") == "display: none;":
                result = logPassword("testInvalidWarranty phase : Input is 'Empty'",filename)
            elif spans[1].get_attribute("style") == "display: none;":
                result = logPassword("testInvalidWarranty phase : Input is 'Too short'",filename)
            elif spans[2].get_attribute("style") ==" display: none;":
                result = logPassword(f"testInvalidWarranty phase : Input '{input}', the input is invalid number",filename)
                
                return result
            
        def testEmpty():
            textarea.click()
            textarea.clear()
            textarea.send_keys(Keys.ENTER)
            sleep(1)
            spans = driver.find_elements("class name",element.SPAN)
            
            if spans[0].get_attribute("style") == "display: none;":
                result = logPassword("testEmpty phase : Empty Msg is not shown",filename)
            elif spans[1].get_attribute("style") == "display: none;":
                result = logPassword("testEmpty phase : Input is 'Too short' ",filename)
            elif spans[2].get_attribute("style") ==" display: none;":
                result = logPassword("testEmpty phase : Input is 'Invalid' ",filename)
                
            return result
    
        def testInputLength():
            
            for i in range(1,6):
                textarea.click()
                textarea.clear()
                textarea.send_keys(randomStrGenerate(i))
                textarea.send_keys(Keys.ENTER)
                sleep(1)
                spans = driver.find_elements("class name",element.SPAN)
                
                if spans[0].get_attribute("style") == "display: none;":
                    result = logPassword("testInputLength phase : Input is 'Empty' ",filename)
                elif spans[1].get_attribute("style") == "display: none;":
                    result = logPassword("testInputLength phase : Input is 'Too short' ",filename)
                elif spans[2].get_attribute("style") ==" display: none;":
                    result = logPassword("testInputLength phase : Input is 'Invalid' ",filename)
                
            textarea.click()
            textarea.clear()
            textarea.send_keys(randomStrGenerate(6))
            textarea.send_keys(Keys.ENTER)
            sleep(1)
            spans = driver.find_elements("class name",element.SPAN)
            
            if spans[0].get_attribute("style") == "display: none;":
                result = logPassword("testInputLength phase : Input is 'Empty'",filename)
            elif spans[1].get_attribute("style") == "display: none;":
                result = logPassword("testInputLength phase : Input is 'Too short' ",filename)
            elif spans[2].get_attribute("style") ==" display: none;":
                result = logPassword("testInputLength phase : Input is 'Invalid' ",filename)
            
            return result
    
        def testLengthAndInvalid():
            textarea.click()
            textarea.clear()
            input = randomSymGenerate(3)
            textarea.send_keys(input)
            textarea.send_keys(Keys.ENTER)
            sleep(1)
            spans = driver.find_elements("class name",element.SPAN)
            
            if spans[0].get_attribute("style") == "display: none;":
                result = logPassword("testLengthAndInvalid phase : Input is 'Empty' ",filename)
            elif spans[1].get_attribute("style") == "display: none;":
                result = logPassword("testLengthAndInvalid phase : Input is 'Too short' ",filename)
            elif spans[2].get_attribute("style") ==" display: none;":
                result = logPassword(f"testLengthAndInvalid phase : Input '{input}', Input is 'invalid' ",filename)
                
            return result


if __name__ == "__main__":
    
    filename = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M") + '.txt'
    testcaseItem = ["testInvalidWarranty","testEmpty","testInputLength","testLengthAndInvalidInput","testValidWarranty"]
    if sys.platform ==  "win32":
        service = chromeService(r"./chromedriver")
    elif sys.platform ==  "darwin":
        service = safariService(r"/usr/bin/safaridriver")
        
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(10)
    driver.get(element.LINK)
    driver.find_element("id",element.COOKIE_BTN).click()
    textarea = driver.find_element("id",element.TEXTAREA)
        
        
    for i ,item in enumerate(testcaseItem):
        
        if item == "testInvalidWarranty":
            warrantyCheck.testInvalidWarranty()
        elif item == "testEmpty":
            warrantyCheck.testEmpty()
        elif item == "testInputLength":
            warrantyCheck.testInputLength()
        elif item == "testLengthAndInvalidInput":
            warrantyCheck.testLengthAndInvalidInput()
        elif item == "testValidWarranty":
            warrantyCheck.testValidWarranty()
    driver.close()
