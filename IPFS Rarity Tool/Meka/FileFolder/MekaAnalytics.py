import pandas as pd
import numpy as np

from Config import project_info, outputFileInfo

itemsInCollection = project_info()
outputFile = outputFileInfo()

# parse text file outputs from Meka.py scripts
def file1():
    namesFile1 = open(r"[scrub]\Python\IPFS Rarity Tool\Meka\txtdump\names1.txt","r")
    namesList1 = namesFile1.read().split("|||")
    namesFile1.close()
    namesList1.remove('')

    traitsFile1 = open(r"[scrub]\Python\IPFS Rarity Tool\Meka\txtdump\traits1.txt","r")
    traitsList1 = traitsFile1.read().split("|||")
    traitsFile1.close()
    traitsList1.remove('')

    return namesList1, traitsList1

# parse text file outputs from Meka.py scripts
def file2():
    namesFile2 = open(r"[scrub]\Python\IPFS Rarity Tool\Meka\txtdump\names2.txt","r")
    namesList2 = namesFile2.read().split("|||")
    namesFile2.close()
    namesList2.remove('')    

    traitsFile2 = open(r"[scrub]\Python\IPFS Rarity Tool\Meka\txtdump\traits2.txt","r")
    traitsList2 = traitsFile2.read().split("|||")
    traitsFile2.close()
    traitsList2.remove('')

    return namesList2, traitsList2

# parse text file outputs from Meka.py scripts
def file3():
    namesFile3 = open(r"[scrub]\Python\IPFS Rarity Tool\Meka\txtdump\names3.txt","r")
    namesList3 = namesFile3.read().split("|||")
    namesFile3.close()
    namesList3.remove('')

    traitsFile3 = open(r"[scrub]\Python\IPFS Rarity Tool\Meka\txtdump\traits3.txt","r")
    traitsList3 = traitsFile3.read().split("|||")
    traitsFile3.close()
    traitsList3.remove('')

    return namesList3, traitsList3

# parse text file outputs from Meka.py scripts
def file4():
    namesFile4 = open(r"[scrub]\Python\IPFS Rarity Tool\Meka\txtdump\names4.txt","r")
    namesList4 = namesFile4.read().split("|||")
    namesFile4.close()
    namesList4.remove('')

    traitsFile4 = open(r"[scrub]\Python\IPFS Rarity Tool\Meka\txtdump\traits4.txt","r")
    traitsList4 = traitsFile4.read().split("|||")
    traitsFile4.close()
    traitsList4.remove('')

    return namesList4, traitsList4

# parse text file outputs from Meka.py scripts
def file5():
    namesFile5 = open(r"[scrub]\Python\IPFS Rarity Tool\Meka\txtdump\names5.txt","r")
    namesList5 = namesFile5.read().split("|||")
    namesFile5.close()
    namesList5.remove('')

    traitsFile5 = open(r"[scrub]\Python\IPFS Rarity Tool\Meka\txtdump\traits5.txt","r")
    traitsList5 = traitsFile5.read().split("|||")
    traitsFile5.close()
    traitsList5.remove('')

    return namesList5, traitsList5

# parse text file outputs from Meka.py scripts
def file6():
    namesFile6 = open(r"[scrub]\Python\IPFS Rarity Tool\Meka\txtdump\names6.txt","r")
    namesList6 = namesFile6.read().split("|||")
    namesFile6.close()
    namesList6.remove('')

    traitsFile6 = open(r"[scrub]\Python\IPFS Rarity Tool\Meka\txtdump\traits6.txt","r")
    traitsList6 = traitsFile6.read().split("|||")
    traitsFile6.close()
    traitsList6.remove('')

    return namesList6, traitsList6

# parse text file outputs from Meka.py scripts
def file7():
    namesFile7 = open(r"[scrub]\Python\IPFS Rarity Tool\Meka\txtdump\names7.txt","r")
    namesList7 = namesFile7.read().split("|||")
    namesFile7.close()
    namesList7.remove('')

    traitsFile7 = open(r"[scrub]\Python\IPFS Rarity Tool\Meka\txtdump\traits7.txt","r")
    traitsList7 = traitsFile7.read().split("|||")
    traitsFile7.close()
    traitsList7.remove('')

    return namesList7, traitsList7

# parse text file outputs from Meka.py scripts
def file8():
    namesFile8 = open(r"[scrub]\Python\IPFS Rarity Tool\Meka\txtdump\names8.txt","r")
    namesList8 = namesFile8.read().split("|||")
    namesFile8.close()
    namesList8.remove('')

    traitsFile8 = open(r"[scrub]\Python\IPFS Rarity Tool\Meka\txtdump\traits8.txt","r")
    traitsList8 = traitsFile8.read().split("|||")
    traitsFile8.close()
    traitsList8.remove('')

    return namesList8, traitsList8

# combines all text file data created by Meka.py scripts
def join(n1, t1, n2, t2, n3, t3, n4, t4, n5, t5, n6, t6, n7, t7, n8, t8):
    finalNamesList = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
    finalTraitsList = t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8
    
    return finalNamesList, finalTraitsList

def df(a, b):
    # create dataframe layout
    finalList = pd.DataFrame(np.column_stack([a, b]), columns=['name', 'trait_attrib_pair'])

    # get sum of trait-attribute pairs that exist in collection and determine frequency (rarity) of those pairs
    rarityDf = pd.DataFrame(finalList.trait_attrib_pair.value_counts().reset_index(name='Sum of Trait Type'))
    rarityDf["Percent Occurrence"] = rarityDf["Sum of Trait Type"] / itemsInCollection

    # write rarity analytics to excel file for review
    with pd.ExcelWriter(outputFile) as writer:
        finalList.to_excel(writer, sheet_name="List")
        rarityDf.to_excel(writer, sheet_name="Rarity_Count")

# call functions to read names and traits from files
namesList1, traitsList1 = file1()
namesList2, traitsList2 = file2()
namesList3, traitsList3 = file3()
namesList4, traitsList4 = file4()
namesList5, traitsList5 = file5()
namesList6, traitsList6 = file6()
namesList7, traitsList7 = file7()
namesList8, traitsList8 = file8()

# compile all files of names and traits and attributes
finalNamesList, finalTraitsList = join(namesList1, traitsList1, namesList2, traitsList2, namesList3, traitsList3, namesList4, traitsList4, namesList5, traitsList5, namesList6, traitsList6, namesList7, traitsList7, namesList8, traitsList8)

# convert to dataframe and output to excel with project analytics
df(finalNamesList, finalTraitsList)