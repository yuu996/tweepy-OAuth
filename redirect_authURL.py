import tweepy

Consumer_Key = "DYblEoQe09595JUH3zez278dX"
Consumer_Secret = "4HWIWPcTJlCWENY8tKdhv2JXOS0SsFpl0qAL9FflEva1Xr8IAZ"
Access_Token = "your access_token"
Access_Token_Secret = "your access_token_secret"

auth = tweepy.OAuth1UserHandler(Consumer_Key,Consumer_Secret)
auth.set_access_token(Access_Token,Access_Token_Secret)
api = tweepy.API(auth)

#get Authorization URL
try:
    redirect_url = auth.get_authorization_url()
    print("Redirect_URL : ", redirect_url)
except Exception as e:
    print('Error!\nFailed to get request token!')
    print(e)
