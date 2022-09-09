The intent of this script was to monitor the HypernovaGroup Twitter account when the account admin was providing discord keys to a private discord group via tweets on twitter. These keys went FAST - like within the minute they were posted to the account, so I built something faster.

The script would monitor for changes in the latest status submitted by the account, and with each new status would check if there was a key. If there was a key, a selenium browser would open automatically, log into discord, connect to the private discord's login page, paste the key, and submit with my account info.

Upon successful submission I would receive a text on my phone notifying me.

I left this script running while grocery shopping when I received the SMS notification, when I came home I saw I had access to the private discord group.