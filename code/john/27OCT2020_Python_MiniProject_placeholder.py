##############################################################################
# John Fial, PDX Code Guild, 2020-2021
# 
# Background:
# 1: I own an Oura smart-ring sleep tracker, which also tracks temperature and other data. 
# Earlier this year, all owners were asked to enter a UCSF TemPredict study for COVID-19.
# Participants fill out a daily survey with any symptoms, any COVID test results, and any manual temperature checks.
# 
# Description: 
# 1: This web automation file prompts me for any health changes before opening a daily web survey for a UCSF study. If I answer 'n' (no changes), it opens the website and clicks the default buttons for me, finishing the survey.
# 2: If I answer 'y' to anything, it opens the webpage for me to fill out appropriately.
# 2: This requires the Selenium module and its Firefox addon installed.
# 
# Notes: This POSTED file has removed my URL, for both privacy and to keep the study data intact. 
##############################################################################

import inspect
def line_number():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

# See https://pypi.org/project/selenium/ for bindings 
# and http://www.seleniumhq.org/ for WebDriver, which does the work
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time # time.sleep(5) is 5-second wait

while True:
    print('Have you experienced any of the following symtoms since last doing the survey? : \n Fever \n Chills \n Fatigue \n General Aches and Pains \n Dry Cough \n Sore Throat \n Cough with Mucus \n Cough with Blood \n Runny / Stuffy Nose \n Swollen / Red Eyes \n Headache \n Unexpected Loss of Smell or Taste \n Loss of Appetite \n Nausea / Vomiting \n Diarrhea')
    print('...OR have you taken any COVID-19 Test since last doing the survey?')
    print('...OR, finally, have you manually taken your temperature since last doing the survey?')

    user_input = input('y/n > ')
    if user_input in ['y', 'n', 'exit']:
        
        if user_input == 'y':
            print('Opening webpage for manual input...')

            with webdriver.Firefox() as driver:
                wait = WebDriverWait(driver, 10)
                driver.get("https://www.google.com")
                
                print('45 second timer started...')
                time.sleep(45)
            break

        elif user_input == 'n':
            ##############################################################################
            print('Running automation...')
            ##############################################################################

            with webdriver.Firefox() as driver:
                wait = WebDriverWait(driver, 10) # Q Understand this wait better...

                driver.get("https://www.google.com")
                
                print(f'LINE #: {line_number()} 5s timer...')
                time.sleep(5)  
                
                # NOTE KEYS.* SHOULD BE CAPITAL LETTERS!
                driver.find_element(By.ID, "NextButton").send_keys((Keys.TAB * 2) + Keys.SPACE) # uses Tabs to select 'No, I have not...'
                driver.find_element(By.ID, "NextButton").send_keys(Keys.SPACE)  # ADVANCES 'NEXT' TO PAGE TWO

                print(f'LINE #: {line_number()} ~~~ PAGE TWO ~~~ ')
                print(f'LINE #: {line_number()} 3s timer...')
                time.sleep(3)  
                driver.find_element(By.ID, "NextButton").send_keys((Keys.TAB * 3) + Keys.SPACE)
                driver.find_element(By.ID, "NextButton").send_keys(Keys.SPACE) # ADVANCES 'NEXT' TO PAGE THREE
                
                print(f'LINE #: {line_number()} ~~~ PAGE THREE ~~~ ')
                print(f'LINE #: {line_number()} 3s timer...')
                time.sleep(3)
                driver.find_element(By.ID, "NextButton").send_keys((Keys.TAB * 3) + Keys.SPACE)
                driver.find_element(By.ID, "NextButton").send_keys(Keys.SPACE) # FINISHES PAGE THREE AND SUBMITS
                print(f'LINE #: {line_number()} PAGE THREE: Is \'I did not take my temperature...\' selected?')

                print(f'LINE #: {line_number()} 15s timer before closing...')
                time.sleep(15)  
            break
        elif user_input == 'exit':
            break
    else: # any other input than 'y' or 'n'
        print('Invalid input. Goodbye.')
        break


# NOTES and TODO:
    ##############################################################################
    # TODO PRINT A PROGRESS TIMER WHILE WAITING...
    # TODO PRINT AND SAVE HISTORY OF DOING THE SURVEY, date/time, AND ITS RESULTS...
    # TODO: OPEN/CLOSE FIREFOX...OPENS IN WIERD NON-USER WINDOW, not incognito but not user-logged in...
    ##############################################################################
print(f'LINE #: {line_number()}    >> PROGRAM ENDED <<    ')

