from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] (%(levelname)s) - %(message)s", datefmt="%d/%m/%Y %H:%M:%S")

pyszne_address = 'https://www.pyszne.pl/'
chrome = webdriver.Chrome(executable_path='C:\chromedriver.exe')
chrome.maximize_window()
chrome.get(pyszne_address)
logging.info("Pyszne.pl homepage opened")

#Zadanie dodatkowe cookie
logging.warning("Waiting for cookie acceptance button may result in an error")
try:
    cookie_button = WebDriverWait(chrome, 3).until(expected_conditions.presence_of_element_located(
        (By.XPATH, '//*[@class="cc-banner"]/section[1]/article[1]/button')))
    cookie_button.click()
    logging.info("Clicked on accept cookies button")
except:
    logging.error("Error while waiting for cookie acceptance button")

time.sleep(1)
pyszne = chrome.find_element_by_xpath('//*[@id="imysearchstring"]')
pyszne.click()
logging.info("Clicked on search bar")
pyszne.send_keys("Brzegi 55, Gdańsk")
logging.info("Typed a location")
time.sleep(1)
pyszne.send_keys(Keys.ENTER)
logging.info("Accepted to search restaurants")
time.sleep(8)
pyszne = chrome.find_element_by_xpath('//*[@data-qa="restaurant-card-element"][1]')
pyszne.click()
logging.info("Clicked on the first restaurant")
time.sleep(2)
pyszne = chrome.find_element_by_xpath('//*[@data-qa="popular-items-list"]/div[1]')
pyszne.click()
logging.info("Clicked on the first product in the popular list")
time.sleep(2)
pyszne = chrome.find_element_by_xpath('//*[@data-qa="item-choices-action-submit"]')
pyszne.click()
logging.info("Accepted the product")

logging.warning("Searching for a product in a cart may result in an error")
try:
    assert chrome.find_element_by_xpath('//*[@data-qa="cart"]')
    logging.info("Item in cart, Pyszne.pl test successful")
except AssertionError:
    logging.error("No items in a cart")
