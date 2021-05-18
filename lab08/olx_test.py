from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

olx_address = 'https://www.olx.pl/'
chrome = webdriver.Chrome(executable_path='C:\chromedriver.exe')
chrome.maximize_window()
chrome.get(olx_address)
olx = chrome.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
olx.click()
olx = chrome.find_element_by_xpath('//*[@id="headerSearch"]')
olx.send_keys("Lego")
olx = chrome.find_element_by_xpath('//*[@id="cityField"]')
olx.send_keys("Gdańsk")
time.sleep(1)
olx.send_keys(Keys.ENTER)
olx.send_keys(Keys.ENTER)
time.sleep(3)
olx = chrome.find_element_by_xpath('//*[@class="offer-wrapper"][1]/table[1]/tbody[1]/tr[1]/td[1]/a[1]')
olx.click()

try:
    assert chrome.find_element_by_xpath('//*[@data-cy="ad_description"]')
    print("Description of item exists, olx.pl test passed")
except AssertionError:
    print("Description of item doesn't exist")
