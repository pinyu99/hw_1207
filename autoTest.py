#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
autoTest.py 

This module simulates the real operation and runs the automation
testing for the warranty checking function.

Before running the test, please download the correct webdriver and
make sure "selenium 4.3.0" is correctly installed. 

'''

import sys
import json
import string
import random
import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as cService
from selenium.webdriver.safari.service import Service as sService

import element


def logPassword(password, filename):
    f = open(filename, "a")
    f.write("{0} -- {1}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), password))
    f.close()

def randomSymGenerate(size:int)->str:
    '''
    Generate random characters for testing

    param size: int, length of generated string
    '''
    special = string.punctuation
    specialStr = random.sample(special,size)
    random.shuffle(specialStr)
    return ''.join(specialStr)

def randomStrGenerate(size:int)->str:
    '''
    Generate random characters for testing

    param size: int, length of generated string
    '''
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))

    
def testValidSerialNumber():
    jsonFilePath = "ValidSerial.json"
    f = open(jsonFilePath)
    data = json.load(f)
    f.close()
    for key, val in data.items():
        #driver.find_element("id",ui.TEXTAREA).click()
        textarea.click()
        textarea.clear()
        textarea.send_keys(val)
        textarea.send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
        serialNumber_found = True
        try:
            rst_item = driver.find_element("class name",element.RST_ITEM)
        except NoSuchElementException:
            serialNumber_found = False
            
        if serialNumber_found == True:
            result = logPassword(f"testValidSerialNumber phase : SerialNumber {val} found",filename)
        else:
            result = logPassword(f"testValidSerialNumber phase : SerialNumber {val} not found",filename)
            
    return result


def testInvalidInput():
    textarea.click()
    textarea.clear()
    input = randomSymGenerate(6)
    textarea.send_keys(input)
    textarea.send_keys(Keys.ENTER)
    sleep(1)
    spans = driver.find_elements("class name",element.SPAN)
    
    if spans[0].get_attribute("style") == "display: none;":
        result = logPassword("testInvalidInput phase : Input is 'Empty'",filename)
    elif spans[1].get_attribute("style") == "display: none;":
        result = logPassword("testInvalidInput phase : Input is 'Too short'",filename)
    elif spans[2].get_attribute("style") ==" display: none;":
        result = logPassword(f"testInvalidInput phase : Input '{input}', the inpur is invalid number",filename)
        
    return result
        
def testEmptyInput():
    textarea.click()
    textarea.clear()
    textarea.send_keys(Keys.ENTER)
    sleep(1)
    spans = driver.find_elements("class name",element.SPAN)
    
    if spans[0].get_attribute("style") == "display: none;":
        result = logPassword("testEmptyInput phase : Empty Msg is not shown",filename)
    elif spans[1].get_attribute("style") == "display: none;":
        result = logPassword("testEmptyInput phase : Input is 'Too short' ",filename)
    elif spans[2].get_attribute("style") ==" display: none;":
        result = logPassword("testEmptyInput phase : Input is 'Invalid' ",filename)
        
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

def testLengthAndInvalidInput():
    textarea.click()
    textarea.clear()
    input = randomSymGenerate(3)
    textarea.send_keys(input)
    textarea.send_keys(Keys.ENTER)
    sleep(1)
    spans = driver.find_elements("class name",element.SPAN)
    
    if spans[0].get_attribute("style") == "display: none;":
        result = logPassword("testLengthAndInvalidInput phase : Input is 'Empty' ",filename)
    elif spans[1].get_attribute("style") == "display: none;":
        result = logPassword("testLengthAndInvalidInput phase : Input is 'Too short' ",filename)
    elif spans[2].get_attribute("style") ==" display: none;":
        result = logPassword(f"testLengthAndInvalidInput phase : Input '{input}', Input is 'invalid' ",filename)
        
    return result
        

if __name__ == "__main__":
    
    filename = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M") + '.txt'
    testcaseItem = ["testInvalidInput","testEmptyInput","testInputLength","testLengthAndInvalidInput","testValidSerialNumber"]
    if sys.platform ==  "win32":
        s = cService(r"./chromedriver")
    elif sys.platform ==  "darwin":
        s = sService(r"/usr/bin/safaridriver")
        
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(10)
    driver.get(element.LINK)
    driver.find_element("id",element.COOKIE_BTN).click()
    textarea = driver.find_element("id",element.TEXTAREA)
        
        
    for i ,item in enumerate(testcaseItem):
        
        if item == "testInvalidInput":
            testInvalidInput()
        elif item == "testEmptyInput":
            testEmptyInput()
        elif item == "testInputLength":
            testInputLength()
        elif item == "testLengthAndInvalidInput":
            testLengthAndInvalidInput()
        elif item == "testValidSerialNumber":
            testValidSerialNumber()
    driver.close()
