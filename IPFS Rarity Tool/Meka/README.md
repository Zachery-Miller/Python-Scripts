Intent of this project was to utilize the IPFS (decentralized file share) to extract NFT project rarity data during project reveals to snipe rare NFTs on sale on Opensea

I created the first iteration of this project the night before a big project reveal when the idea came to me and copy pasted a bulk of the code (not shared here) and modified it to use for several other NFT project reveals.

Running the Meka.bat file will concurrently run all 8 Meka.py scripts and scrape the underlying JSON data for each NFT from the IPFS link where the project is hosted.
Running the Analytics.bat file once Meka.py scripts finish running will combine all output text files into a singular excel output with the rare traits and attributes of the NFT project and the corresponding token ID to search in Opensea.

There are obvious flaws in the design of this project - but this very rough around the edges project worked incredibly in obtaining rare NFTs from popular projects during the 2021 bull run.