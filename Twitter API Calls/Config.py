import tweepy as tp
import os

from twilio.rest import Client

def api_config():
    # get API info from env variables
    api_key = os.getenv('TWITTER_API_KEY')
    api_secret = os.getenv('TWITTER_API_SECRET')
    access_token = os.getenv('TWITTER_ACCESS_TKN')
    access_token_secret = os.getenv('TWITTER_ACCESS_TKN_SCRT')

    # authorize access to API and return api as an object
    auth = tp.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tp.API(auth, wait_on_rate_limit=True)
    return api

# configure twilio for SMS to my cell phone [scrubbed] 
def twllio_config():
    client = Client("scrub",
                    "scrub")
    return client