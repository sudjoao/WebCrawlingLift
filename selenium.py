from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

chrome_driver_path = r"C:\Users\Gustavo Afonso\Desktop\ChromeDriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_driver_path)
#browser = webdriver.Chrome()

browser.get("https://www.python.org/")

nav = browser.find_element_by_id("mainnav")

time.sleep(10)
print(nav.text)

