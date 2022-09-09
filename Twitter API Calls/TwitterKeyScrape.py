import tweepy as tp
import time as time
import datetime as datetime
import os as os
import webbrowser

from Config import api_config, twllio_config
from AutomatedHyperNovaOpen import discord_login, discord_authorization, paste_key, init

# authentication
api = api_config()
client = twllio_config()

# global variables
webpage = 'https://dash.hypernova.group/dashboard'
twitter_account = 'HypernovaGroup'
tweet_count = 1
start_status = api.user_timeline(twitter_account, count = tweet_count)
key_found = False



def key_gen(key):
    # search tweet for hyphens
    index = key.find('-')

    # slice key from start to finish based on first hyphen found
    full_key = key[index-5:index+18]
    return full_key

def get_status():
    # sleep delay to respect rate limit
    time.sleep(3) 

    # get the current status for account monitored and return it
    user_current_status = api.user_timeline(twitter_account, count = tweet_count)
    return user_current_status[0].text

def get_last_status():
    # get previous status for account monitored and return it
    last_status = start_status[0].text
    return last_status

def key_check(key):
    # check hyphen exists in 11th element of string to validate key format
    if key[11] == '-':
        key_legit = True
        return key_legit
    else:
        key_legit = False
        return key_legit

def key_to_notepad(key):
    # write key from tweet into notepad file
    f = open("key.txt","w+")
    f.write(key)
    os.startfile(r'key.txt')

def open_hypernova_chrome(webpage):
    # open webpage with selenium
    webbrowser.open(webpage)


def sms_notification(key):
    # send text notification
    client.messages.create(to="+scrub",
                           from_="+scrub",
                           body= ".\n\r" + key + "\n\r" + webpage)

def new_tweet():
    # send text notification when new tweet comes out
    client.messages.create(to="+scrub",
                           from_="+scrub",
                           body= ".\n\r" + "NEW TWEET" + "\n\r")

# set last status to a variable for comparisons 
prev_status = get_last_status()

# loop while key has not been scraped from tweets
while key_found != True:
    current_status = get_status()

    # check new tweet for key and call functions
    if current_status != prev_status:
        if '-' in current_status:
            prev_status = current_status
            key = key_gen(current_status)
            key_found = key_check(key)
        else:
            prev_status = current_status
            new_tweet()

    # checks if tweet is still the same
    elif '-' in current_status and current_status == prev_status:
        print('Still running!' + str(datetime.datetime.now()))
        continue
    
    # checks if tweet is still the same
    else:
        prev_status = current_status
        print('Still running!' + str(datetime.datetime.now()))


# manual/verification function calls [if web browser automation fails]
key_to_notepad(key)
open_hypernova_chrome(webpage)
sms_notification(key)

# automated function calls [intended use]
browser = init()
discord_login(browser)
discord_authorization(browser)
paste_key(browser, key)



