from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

#OLX Scenario 1

olx = 'https://www.olx.pl/'
chrome = webdriver.Chrome(executable_path='C:\chromedriver.exe')
chrome.maximize_window()
chrome.get(olx)
olx_cookie_accept = chrome.find_element_by_id("onetrust-accept-btn-handler")
olx_cookie_accept.click()
olx_search = chrome.find_element_by_id("headerSearch")
olx_search.send_keys("gundam")
olx_cityfield = chrome.find_element_by_id("cityField")
olx_cityfield.send_keys("Gdańsk")
time.sleep(1)
olx_cityfield.send_keys(Keys.ENTER)
olx_cityfield.send_keys(Keys.ENTER)
time.sleep(1)
try:
    assert "Gundam w Gdańsk" in chrome.title
    print("Correct title, test number 1 passed")
except AssertionError:
    print("Title is not correct")

#OLX Scenario 2

olx_register = 'https://www.olx.pl/konto/#register'
chrome.get(olx_register)
olx_email = chrome.find_element_by_id("userEmailRegister")
olx_email.send_keys("piwo")
olx_email.send_keys(Keys.ENTER)
time.sleep(1)
try:
    olx_error = chrome.find_element_by_class_name("error")
    print("Error appeared, test number 2 passed")
except NoSuchElementException:
    print("Error doesn't appear")

#OLX Scenario 3

chrome.get(olx)
olx_apps = chrome.find_element_by_id("footerLinkMobileApps")
olx_apps.click()
try:
    olx_app_icons = chrome.find_element_by_class_name("app-icons")
    print("App icons exist, test number 3 passed")
except NoSuchElementException:
    print("App icons don't exist")
