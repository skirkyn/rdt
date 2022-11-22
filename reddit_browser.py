import json
import random
import re
import time
import reddit_api

import random
import password_generator
import requests
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# username = 'Fun_Shame_6062'
# password = 't=S=W$t04nOrg&wU'


def login(driver, username, password):
    driver.get('https://www.reddit.com/login')
    login_input = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.ID, 'loginUsername')))
    login_input.send_keys(username)
    time.sleep(10 * random.random())

    password_input = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.ID, 'loginPassword')))
    password_input.send_keys(password)
    time.sleep(10 * random.random())
    login_button = WebDriverWait(driver, timeout=10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Log In")]')))
    login_button.click()
    WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.ID, 'SearchDropdown')))


def get_token(driver, username, password):
    login(driver, username, password)
    driver.get('view-source:https://www.reddit.com/')
    the_text = WebDriverWait(driver, timeout=10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[@class="html-attribute-value" and text() = "data"]/../..')))
    return json.loads(the_text.text[49:-18])['user']['session']['accessToken']


def get_driver(
        user_agent=f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{random.randint(10, 16)}_0) AppleWebKit/521.36 (KHTML, like Gecko) Chrome/{random.randint(103, 108)}.1.0.0 Safari/537.36"):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("user-agent=" + user_agent)

    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        chrome_options=chrome_options)  # webdriver.Chrome('/Users/anya/Downloads/chromedriver')


ua = f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{random.randint(10, 16)}_0) AppleWebKit/521.36 (KHTML, like Gecko) Chrome/{random.randint(103, 108)}.1.0.0 Safari/537.36"
# driver = get_driver()
# token = get_token(driver, username, password)
# reddit_api.vote('-1', 't1_iwgm092', token, ua)
