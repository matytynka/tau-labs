from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Pyszne Scenario

pyszne = 'https://www.pyszne.pl/'
chrome = webdriver.Chrome(executable_path='C:\chromedriver.exe')
chrome.maximize_window()
chrome.get(pyszne)
time.sleep(1)
pyszne_address = chrome.find_element_by_xpath('//*[@id="imysearchstring"]')
pyszne_address.click()
pyszne_address.send_keys("Brzegi 55, Gdańsk")
time.sleep(1)
pyszne_address.send_keys(Keys.ENTER)
time.sleep(7)
pyszne_address = chrome.find_element_by_xpath('//*[@data-qa="restaurant-card-element"][1]')
pyszne_address.click()
time.sleep(2)
pyszne_address = chrome.find_element_by_xpath('//*[@data-qa="popular-items-list"]/div[1]')
pyszne_address.click()
time.sleep(2)
pyszne_address = chrome.find_element_by_xpath('//*[@data-qa="item-choices-action-submit"]')
pyszne_address.click()

try:
    assert chrome.find_element_by_xpath('//*[@data-qa="cart"]')
    print("Item in cart, test number 1 passed")
except AssertionError:
    print("No item in cart")
time.sleep(1)
