#Only need to update projectIPFS and number of items in the collection both can be found on etherscan contract

def ipfs():
    base_url = "https://ipfs.io/ipfs/"
    backup_base_url = "https://gateway.pinata.cloud/ipfs/"
    projectIPFS = "scrub/metadata/"
    # return backup base url and modify main script if new gateway required
    return(base_url, backup_base_url, projectIPFS) 

def project_info():
    itemsInCollection = 8888
    return(itemsInCollection)

def outputFileInfo():
    outputFile = "Meka_output.xlsx"
    return outputFile