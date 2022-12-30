import tweepy
from requests_oauthlib import OAuth1Session
import urllib.parse

consumer_key = "Your Consumer Key"
consumer_secret = "Your Consumer Secret"
auth = tweepy.OAuth1UserHandler(consumer_key,consumer_secret)
url = input("Input The URL after Redirect : ")
url_parse = urllib.parse.parse_qs(url)

token = url_parse['https://twitter.com/home?oauth_token'][0]
verifier = url_parse['oauth_verifier'][0]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.request_token = { 'oauth_token' : token,'oauth_token_secret' : verifier }

try:
    access_token = auth.get_access_token(verifier)
    print("access_token = ",auth.access_token)
    print("access_token_secret = ",auth.access_token_secret)
except Exception as e:
    print('Error! \nFailed get Access Token!')
    print(e)