import tweepy
import urllib.parse

Consumer_Key = "Your Consumer Key"
Consumer_Secret = "Your Consumer Secret"
url = input("Input The URL after Redirect : ")
url_parse = urllib.parse.parse_qs(url)

token = url_parse['https://twitter.com/home?oauth_token'][0] #get oauth_token in URL
verifier = url_parse['oauth_verifier'][0] #get oauth_verifier in URL

auth = tweepy.OAuth1UserHandler(Consumer_Key,Consumer_Secret)
auth.request_token = { 'oauth_token' : token,'oauth_token_secret' : verifier }

try:
    access_token = auth.get_access_token(verifier)
    print("Access_Token = ",auth.access_token)
    print("Access_Token_secret = ",auth.access_token_secret)
except Exception as e:
    print('Error! \nFailed get Access Token!')
    print(e)