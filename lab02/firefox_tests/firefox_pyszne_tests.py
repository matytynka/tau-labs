from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Pyszne Scenario 1

pyszne = 'https://www.pyszne.pl/'
firefox = webdriver.Firefox(executable_path='C:\geckodriver.exe')
firefox.maximize_window()
firefox.get(pyszne)
time.sleep(1)
pyszne_address = firefox.find_element_by_id("imysearchstring")
pyszne_address.click()
pyszne_address.send_keys("Brzegi 55, Gdańsk")
time.sleep(1)
pyszne_address.send_keys(Keys.ENTER)
time.sleep(7)
try:
    assert "Gdansk" in firefox.title
    print("Correct title, test number 1 passed")
except AssertionError:
    print("Title is not correct")
time.sleep(1)

#Pyszne Scenario 2

firefox.get(pyszne)
pyszne_city = firefox.find_element_by_css_selector("a[class='tabslider-links'][title='Kraków']")
pyszne_city.click()
pyszne_area = firefox.find_element_by_css_selector("a[title='Zamów jedzenie online  Kraków (Kraków Nowa Huta)']")
pyszne_area.click()
time.sleep(2)
try:
    assert "Kraków-Nowa Huta" in firefox.find_elements_by_css_selector("h1")[2].text
    print("Correct title in h1, test number 2 passed")
except AssertionError:
    print("Title is not correct")

#Pyszne Scenario 3

firefox.get(pyszne)
pyszne_lang = firefox.find_element_by_id("locale")
pyszne_lang.click()
pyszne_eng = firefox.find_element_by_css_selector("a[class='js-click-language js-url-source'][data-click-language='en']")
pyszne_eng.click()
time.sleep(2)
try:
    assert "https://www.pyszne.pl/en/" in firefox.current_url
    print("Correct url, test number 3 passed")
except AssertionError:
    print("Url is not correct")
