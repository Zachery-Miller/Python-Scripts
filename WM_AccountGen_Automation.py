import time as time
import datetime as datetime
import os as os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def init():
    browser = webdriver.Chrome(executable_path=r'C:\bin\chromedriver.exe')
    browser.implicitly_wait(15) # wait's for the page to get done loading before it does anything with it
    browser.get('https://www.walmart.com/account/signup')
    return browser

def list_create():
    count = 0
    lines = []
    new_lines = []

    #format
    #FirstName:LastName:Email:Password

    with open('emails.txt') as f:
        lines = f.readlines()
    for line in lines:
        new_lines.append(line.split(':'))
        count += 1
    return(new_lines,count)

def sign_up(br, accounts, iteration):
    time.sleep(10)
    firstName = br.find_element_by_name('firstName')
    firstName.send_keys(accounts[iteration][0])

    lastName = br.find_element_by_name('lastName')
    lastName.send_keys(accounts[iteration][1])

    email = br.find_element_by_id('email-su')
    email.send_keys(accounts[iteration][2])

    password = br.find_element_by_id('password-su')
    password.send_keys(accounts[iteration][3])

    rememberMe = br.find_element_by_xpath('//*[@id="remember-me-su"]')
    action1 = webdriver.common.action_chains.ActionChains(br)
    action1.move_to_element_with_offset(rememberMe, -15, 0)
    action1.click()
    action1.perform()

    try:
        newsLetter = br.find_element_by_xpath('//*[@id="su-newsletter"]')
        action2 = webdriver.common.action_chains.ActionChains(br)
        action2.move_to_element_with_offset(newsLetter, -15, 0)
        action2.click()
        action2.perform()

    except:
        pass

    try:
        createAccount = br.find_element_by_xpath('//*[@id="sign-up-form"]/button[1]')
        createAccount.click()
        print("submitted info")
    except:
        pass

    
    time.sleep(2)

    try:
        pxCaptcha = br.find_element_by_xpath('//*[@id="px-captcha"]')
    except:
        print('NO CAPTCHA FOUND')
        browser.quit()
    else:
        #click and hold code goes here
        print('CAPTCHA FOUND')
        #pxCaptcha_button = br.find_element_by_xpath('//*[@id="px-captcha"]')
        action_click_and_hold = webdriver.common.action_chains.ActionChains(br)
        action_click_and_hold.move_to_element(pxCaptcha)
        print("About to click")
        action_click_and_hold.click_and_hold()
        action_click_and_hold.pause(10)
        action_click_and_hold.release()
        action_click_and_hold.perform()
        print("clicked")
        time.sleep(10)

#Main
accounts, num_accounts = list_create()
for i in range(num_accounts):
    browser = init()
    sign_up(browser, accounts, i)
    browser.quit()
