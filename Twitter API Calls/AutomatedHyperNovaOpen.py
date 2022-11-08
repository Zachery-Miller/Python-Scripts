from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time as time

#start it up
def init():
    browser = webdriver.Chrome(executable_path=r'C:\bin\chromedriver.exe')
    browser.implicitly_wait(15) # wait's for the page to get done loading before it does anything with it
    browser.get('https://dash.hypernova.group/dashboard')
    return browser

def discord_login(br):
    email = br.find_element_by_name('email')
    email.send_keys("scrub")

    password = br.find_element_by_name('password')
    password.send_keys("scrub")

    login_button = br.find_elements_by_class_name("marginBottom8-AtZOdT.button-3k0cO7.button-38aScr.lookFilled-1Gx00P.colorBrand-3pXr91.sizeLarge-1vSeWK.fullWidth-1orjjo.grow-q77ONN")
    login_button[0].click()

def discord_authorization(br):
    auth_button = br.find_elements_by_class_name("button-38aScr.lookFilled-1Gx00P.colorBrand-3pXr91.sizeMedium-1AC_Sl.grow-q77ONN")
    auth_button[0].click()

def paste_key(br, final_key):
    close_pop_up = br.find_elements_by_class_name("pointer.btn.btn-branded.btn-sm.float-right")
    close_pop_up[0].click()
    
    text_box_for_key = br.find_element_by_name('key')
    text_box_for_key.send_keys(final_key)

    activate = br.find_element_by_id('activation_btn')
    activate.click()


    '''
    try:
        element = WebDriverWait(br, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "button-38aScr.lookFilled-1Gx00P.colorBrand-3pXr91.sizeMedium-1AC_Sl.grow-q77ONN")))
    finally:
        br.quit()
    '''



#key = "D3DA4-12C0B-CE210-677A8"
#discord_login()
#discord_authorization()
#paste_key(key)