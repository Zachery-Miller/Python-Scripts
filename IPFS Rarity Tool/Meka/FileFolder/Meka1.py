import json
import pandas as pd
import numpy as np

from os import name
from urllib.request import urlopen
from bs4 import BeautifulSoup
from Config import ipfs, project_info, outputFileInfo

#global lists
mainList = []
singleJSON_List = []
traitType = []
attributeValue = []
nameList = []
tokenIDList = []
traitAndAttributeList = []

#assign project specific variables from config file
base_url, backup_base_url, projectIPFS = ipfs()
itemsInCollection = project_info()
outputFile = outputFileInfo()

#test page open plus json list gen
def scraped_JSON_list_gen():
    for i in range(1, itemsInCollection - 7777):
        url = base_url + projectIPFS + str(i)
        backup_url = backup_base_url + projectIPFS + str(i)

        try:
            page = urlopen(url, timeout=10)
            print(url)
            soup = BeautifulSoup(page, 'html.parser')
            strSoup  = str(soup)
            baseDictionary = json.loads(strSoup)
            mainList.append(baseDictionary)
        except:
            continue
    return(mainList)

#appending sample dictionary JSON to list, used to get number of attributes so iteration is dynamic from project to project   
def find_num_attributes():
    singleJSON_List.append(mainList[0])
    for item in singleJSON_List:
        numAttributes = len(item["attributes"])
    return numAttributes

#get name and attribute value pairs for analysis
def name_trait_attribute_list_gen():
    for NFTi in mainList:

        for i in range(numAttributes):

            #missing attribute handling
            try:
                name_var = NFTi["name"]
                traitType_var = NFTi["attributes"][i]["trait_type"]
                attributeValue_var = NFTi["attributes"][i]["value"]

                nameList.append(name_var)
                traitAndAttributeList.append(traitType_var + ":" + attributeValue_var)

            except:
                continue
    return(nameList, traitAndAttributeList)

def list_to_txt_file():
    names = open(r"C:\Users\zache\OneDrive\Desktop\VS Code Files\Python\IPFS Rarity Tool\Meka\txtdump\names1.txt","w+")
    traits = open(r"C:\Users\zache\OneDrive\Desktop\VS Code Files\Python\IPFS Rarity Tool\Meka\txtdump\traits1.txt","w+")

    #names.write(str(name + "|" for name in nameList))
    for i in nameList:
        names.write(i + "|||")
    names.close()

    for i in traitAndAttributeList:
        traits.write(i + "|||")
    traits.close()

# function calls
mainList = scraped_JSON_list_gen()

# get number of attributes in NFT project
numAttributes = find_num_attributes()

# get names of traits and attributes in NFT project
name_trait_attribute_list_gen()

# output data to text file
list_to_txt_file()



