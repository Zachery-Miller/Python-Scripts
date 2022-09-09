import discord
import time
import os

from discord.webhook import RequestsWebhookAdapter, Webhook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from Proxylist import proxy_list
from random import randint
from selenium.common.exceptions import NoSuchElementException

# pull proxy list from proxy file
proxyList = proxy_list()

# get env variables
discord_id = os.getenv('DISCORD_ID')
webhook = Webhook.from_url(os.getenv("DISCORD_WEBHOOK"), adapter=RequestsWebhookAdapter())

# define url and run value
url = "https://www.gasnow.org/"
run = True

# set delay and max connect attempts before rotating proxies or exiting site
sleepytime = 5
maxConnectAttempts = 25

# select a random proxy from proxy list
proxyNum = randint(0,len(proxyList))

# list of banned proxies
bannedProxies = []

# counter variable
counter = 0

# set chrome options for selenium
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")


def __init__():
    e = ""
    for i in range(maxConnectAttempts):
        try:
            proxyNum = randint(0,len(proxyList))
            chrome_options.add_argument('--proxy-server=%s' % (proxyList[proxyNum]))
            browser = webdriver.Chrome(executable_path=r'C:\bin\chromedriver.exe', options=chrome_options)
            browser.implicitly_wait(15)
            browser.get(url)
            break

        except NoSuchElementException:
            print("Element could not be found")
            continue

        except Exception as e:
            print(e)
            print(proxyNum)
            print(proxyList[proxyNum])
            proxyList.remove(proxyList[proxyNum])
            bannedProxies.append(proxyList[proxyNum])
            continue

    return browser, e

def get_gas(webpage):
    gas_prices = []
    rapid = webpage.find_element_by_xpath('//*[@id="status"]/ul/li[1]/div[1]/strong').text 
    gas_prices.append(rapid)
    fast = webpage.find_element_by_xpath('//*[@id="status"]/ul/li[2]/div[1]/strong').text
    gas_prices.append(fast)
    std = webpage.find_element_by_xpath('//*[@id="status"]/ul/li[3]/div[1]/strong').text
    gas_prices.append(std)
    slow = webpage.find_element_by_xpath('//*[@id="status"]/ul/li[4]/div[1]/strong').text
    gas_prices.append(slow)
    return gas_prices

def fail_embed(failureMessage):
    embed = discord.Embed(title="Failed to fetch gas prices", url="https://www.gasnow.org/", description = failureMessage + "\n" + discord_id, color=discord.Color.blue())
    webhook.send(embed=embed)

def gas_embed():
    embed = discord.Embed(title="Etherscan Black Hole", url="https://etherscan.io/address/0x0000000000000000000000000000000000000000#tokentxnsErc721", description ="Gas is spiking, check black hole address linked above to see whats minting.\n" + discord_id, color=discord.Color.blue())
    embed.add_field(name="Rapid", value=str(current_gas[0]), inline=False)
    embed.add_field(name="Fast", value=str(current_gas[1]), inline=False)
    embed.add_field(name="Standard", value=str(current_gas[2]), inline=False)
    embed.add_field(name="Slow", value=str(current_gas[3]), inline=False)
    webhook.send(embed=embed)

def status_embed():
    embed = discord.Embed(title="Still running", url="https://www.gasnow.org/", description = "Still fetching gas" + "\n" + discord_id, color=discord.Color.blue())
    webhook.send(embed=embed)


# start script
gasNowSite, failException = __init__()
while run == True:
    try:
        # get gas data and convert to list
        gasData = get_gas(gasNowSite)
        current_gas = list(map(int, gasData))
        counter += 1
        

    except:
        # catch any exceptions and restart script
        fail_embed(failException)
        gasNowSite.quit()
        time.sleep(2)
        gasNowSite = __init__()
        time.sleep(3)
        continue

    try:
        # refresh site
        gasNowSite.refresh()
    
    except:
        # catch refresh failed exceptions and restart program
        gasNowSite.quit()
        time.sleep(2)
        gasNowSite, failException = __init__()
        time.sleep(3)
        continue

    time.sleep(sleepytime)

    # call output to discord webhook to notify that program is still running
    if counter >= 100:
        status_embed()
        counter = 0
    else:
        continue

    # call output to discord webhook to notify gas has spiked over 200 gwei
    if current_gas[0] >= 200:
        gas_embed()

    # print gas to terminal
    else:
        print(current_gas)
    
# exit script
gasNowSite.quit()