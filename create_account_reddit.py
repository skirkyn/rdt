import json
import random
import time

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


def register_email():
    create_email_resp = requests.get('https://temporarymail.com/ajax/?action=requestEmailAccess&value=random')
    if not create_email_resp.ok:
        print('Can\'t create email ' + create_email_resp.text)
        exit(1)
    return json.loads(create_email_resp.text)


def wait_for_email(secretKey):
    while True:
        print('Trying to read emails ... ')
        messages = requests.post(
            'https://temporarymail.com/ajax/?action=checkInbox&value={secretKey}'.format(secretKey=secretKey))
        if not messages.ok:
            print('Can\'t read email ' + messages.text)
            exit(1)

        email_list = json.loads(messages.text)
        if not email_list:
           continue

        email_id_list = list(filter(lambda k: email_list[k]['from'] == 'noreply@reddit.com', email_list.keys()))
        if len(email_id_list):
            return email_id_list[0]


def read_link_from_reddit(email_id):
    email_body = requests.get(
        'https://temporarymail.com/view/?i={id}&width=930'.format(id=email_id))
    if not email_body.ok:
        print('Can\'t read email body ' + email_body.text)
        exit(1)

    soup = BeautifulSoup(email_body.text, "html.parser")
    dom = etree.HTML(str(soup))
    return dom.xpath('//*[text()="Verify Email Address"]/../..')[0].get('href').replace('hxxps://', 'https://')


print('Registering new email ... ')
res = register_email()

email = res['address']
secretKey = res['secretKey']

generator = password_generator.PasswordGenerator()
generator.minlen = 8
password = generator.generate()
print(f'Email: {email}, password: {password}')



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/521.36 (KHTML, like Gecko) Chrome/104.1.0.0 Safari/537.36")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    chrome_options=chrome_options)  # webdriver.Chrome('/Users/anya/Downloads/chromedriver')
driver.get('https://www.reddit.com/account/register/')

WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.ID, 'regEmail')))
email_element = driver.find_element(By.ID, 'regEmail')
email_element.send_keys(email)
driver.find_element(By.XPATH,
                    '//button[@data-step="email"]').click()
time.sleep(10 * random.random())
def_name_element = WebDriverWait(driver, timeout=10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div[2]/div/div/div[2]/div[2]/div/div/a[1]')))
user = def_name_element.text
user_name_element = driver.find_element(By.ID, 'regUsername')
user_name_element.send_keys(def_name_element.text)
password_element = driver.find_element(By.ID, 'regPassword')
password_element.send_keys(password)

submit = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div/main/div[2]/div/div/div[3]/button[@data-step="username-and-password"]')))
submit.click()
time.sleep(10 * random.random())


print(f'Successfully registered a user {user}, email: {email}, password: {password}')

with open('users.csv', 'a') as fle:
    fle.writelines('|'.join([user, password, email, '\n']))

print(f'Trying to finish the setup for email {email} ... ')

skip = WebDriverWait(driver, timeout=60).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/header/div[1]/div[2]/button[text()="Skip"]')))
skip.click()
time.sleep(10 * random.random())
WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[1]/div/button[1]'))).click()
time.sleep(10 * random.random())
WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[1]/div/button[2]'))).click()
time.sleep(10 * random.random())
WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[1]/div/button[3]'))).click()
time.sleep(10 * random.random())
WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[2]/button[text()=\'Continue\']'))).click()
time.sleep(10 * random.random())
WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable(
    (By.XPATH,
     '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[1]/div/div[2]/button[text()=\'Select All\']'))).click()
time.sleep(10 * random.random())
WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[2]/button[text()=\'Continue\']'))).click()
time.sleep(10 * random.random())
WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[2]/button[text()=\'Continue\']'))).click()
time.sleep(10 * random.random())
WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.ID, 'USER_DROPDOWN_ID')))

print(f'Verifying the email {email} ... ')
email_id = wait_for_email(secretKey)
link = read_link_from_reddit(email_id)
print(f'Was able to extract the link {link} ... ')
driver.get(link)
verify = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="verify-email"]/button')))
time.sleep(10 * random.random())
verify.click()
driver.get('https://www.reddit.com')

WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.ID, 'USER_DROPDOWN_ID')))
#Treve.Kandoll@AppMailer.org @llowDoit22@ bBAxFSMky65OlgndCXNvt3atKfYdi1p mod.fucker