from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

#OLX Scenario 1

olx = 'https://www.olx.pl/'
edge = webdriver.Edge(executable_path='C:\msedgedriver.exe')
edge.maximize_window()
edge.get(olx)
olx_cookie_accept = edge.find_element_by_id("onetrust-accept-btn-handler")
olx_cookie_accept.click()
olx_search = edge.find_element_by_id("headerSearch")
olx_search.send_keys("gundam")
olx_cityfield = edge.find_element_by_id("cityField")
olx_cityfield.send_keys("Gdańsk")
time.sleep(1)
olx_cityfield.send_keys(Keys.ENTER)
olx_cityfield.send_keys(Keys.ENTER)
time.sleep(1)
try:
    assert "Gundam w Gdańsk" in edge.title
    print("Correct title, test number 1 passed")
except AssertionError:
    print("Title is not correct")

#OLX Scenario 2

olx_register = 'https://www.olx.pl/konto/#register'
edge.get(olx_register)
olx_email = edge.find_element_by_id("userEmailRegister")
olx_email.send_keys("piwo")
olx_email.send_keys(Keys.ENTER)
time.sleep(1)
try:
    olx_error = edge.find_element_by_class_name("error")
    print("Error appeared, test number 2 passed")
except NoSuchElementException:
    print("Error doesn't appear")

#OLX Scenario 3

edge.get(olx)
olx_apps = edge.find_element_by_id("footerLinkMobileApps")
olx_apps.click()
try:
    olx_app_icons = edge.find_element_by_class_name("app-icons")
    print("App icons exist, test number 3 passed")
except NoSuchElementException:
    print("App icons don't exist")
