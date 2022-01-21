from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("/Users/talefronny/Downloads/chromedriver")
browser = webdriver.Chrome(service=s)
url = "https://www.google.com"
browser.get(url)
