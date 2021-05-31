from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] (%(levelname)s) - %(message)s", datefmt="%d/%m/%Y %H:%M:%S")

olx_address = 'https://www.olx.pl/'
chrome = webdriver.Chrome(executable_path='C:\chromedriver.exe')
chrome.maximize_window()
chrome.get(olx_address)
logging.info("OLX homepage opened")
olx = chrome.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
olx.click()
logging.info("Clicked accept on cookie banner")
olx = chrome.find_element_by_xpath('//*[@id="headerSearch"]')
olx.send_keys("Lego")
logging.info("Typed Lego in a search field")
olx = chrome.find_element_by_xpath('//*[@id="cityField"]')
olx.send_keys("Gdańsk")
logging.info("Typed Gdańsk in a city field")
time.sleep(1)
olx.send_keys(Keys.ENTER)
logging.info("Accepted the first proposed location")
olx.send_keys(Keys.ENTER)
logging.info("Accepted to search products")
time.sleep(3)
olx = chrome.find_element_by_xpath('//*[@class="offer-wrapper"][1]/table[1]/tbody[1]/tr[1]/td[1]/a[1]')
olx.click()
logging.info("Clicked on the first product")

logging.warning("Searching for a description may result in an error")
try:
    assert chrome.find_element_by_xpath('//*[@data-cy="ad_description"]')
    logging.info("Description of an item exists, olx.pl test successful")
except AssertionError:
    print("Description of item doesn't exist")
    logging.error("Didn't find a description of an item")
