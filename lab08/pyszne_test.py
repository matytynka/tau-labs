from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

pyszne_address = 'https://www.pyszne.pl/'
chrome = webdriver.Chrome(executable_path='C:\chromedriver.exe')
chrome.maximize_window()
chrome.get(pyszne_address)

#Zadanie dodatkowe cookie
cookie_button = WebDriverWait(chrome, 3).until(expected_conditions.presence_of_element_located(
    (By.XPATH, '//*[@class="cc-banner"]/section[1]/article[1]/button')))
cookie_button.click()

time.sleep(1)
pyszne = chrome.find_element_by_xpath('//*[@id="imysearchstring"]')
pyszne.click()
pyszne.send_keys("Brzegi 55, Gdańsk")
time.sleep(1)
pyszne.send_keys(Keys.ENTER)
time.sleep(7)
pyszne = chrome.find_element_by_xpath('//*[@data-qa="restaurant-card-element"][1]')
pyszne.click()
time.sleep(2)
pyszne = chrome.find_element_by_xpath('//*[@data-qa="popular-items-list"]/div[1]')
pyszne.click()
time.sleep(2)
pyszne = chrome.find_element_by_xpath('//*[@data-qa="item-choices-action-submit"]')
pyszne.click()

try:
    assert chrome.find_element_by_xpath('//*[@data-qa="cart"]')
    print("Item in cart, pyszne.pl test passed")
except AssertionError:
    print("No item in cart")
chrome.implicitly_wait(1)
