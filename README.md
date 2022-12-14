# hw_1207
#autoWarrantyCheck
This module used "selenium" to automate browser for checking product warranty. It provides different browsers and platforms (chrome and safari) to validate automated test, and it will create a .txt result when the test finished. 

Please install a correct webdriver and seleninum module before starting the test. 

##Test Case Type
(1) testValidWarranty: Ensure the valid warranty number can be found. If the warrnaty number not be found, the error message will show in result txt file.
(2) testInvalidWarranty: If the input was invalid, the result will show error message.
(3) testEmpty: Input checking machanisms. If the text area was empty, the result txt file will show error message. 
(4) testInputLength: Input checking machanisms. Check the input's character length, if input length was incorrect, the error message will show. 
(5) testLengthAndInvalid: Input checking machanisms. If the input's character length is not enough and the input is invalid, the result txt file will show error message. 

##Environment Setup
Please install the webdriver corresponding to the version of the browser, and make sure that the webdriver and autoWarrantyCheck.py are in the same directory. 
The autoWarrantyCheck is written in python3, and please make sure autoWarrantyCheck is running in python3.  
