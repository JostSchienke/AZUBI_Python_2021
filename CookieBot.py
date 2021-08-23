from os import truncate
import time
from requests.api import options
from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.chrome.options import Options
import keyboard

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options= options, executable_path= r"C:\Users\josts\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://orteil.dashnet.org/cookieclicker/")

def Click_on_cookie(num):
    Big_cookie = driver.find_element_by_id("bigCookie")
    for i in range(num):
        Big_cookie.click()

time.sleep(10)

while(True):
    Click_on_cookie(1)

    try:
        items = driver.find_elements_by_class_name("enabled")
        for item in items[::-1]:
            item.click()
    except:
        print("Not enough cookies")

    try:
        schims = driver.find_element_by_class_name("shimmer")
        for schim in schims[::-1]:
            schim.click()
    except:
        print("Found No Golden Cookie!") 

    if keyboard.is_pressed("q"):
        break