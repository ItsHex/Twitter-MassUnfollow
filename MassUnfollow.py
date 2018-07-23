#Use pip install Twython if you haven't already, this script won't work otherwise.
from twython import Twython, TwythonError

#Get your Key and oAuth tokens from apps.twitter.com/app/new
app_key = '#####'
app_secret = '#####'
oauth_token = '#####'
oauth_token_secret = '#####'


#Change the "Twitter Handler Here" to your username with NO @
#Count is set to 50 by default, Change at your own risk!
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
mfriends = twitter.get_followers_ids(screen_name='Twitter Handle Here', count=50)
try:
    for unfollo in mfriends['ids']:
        twitter.destroy_friendship(user_id=unfollo)
except TwythonError as e:
    print(e)


#Author: ItsHex
#License: MIT
#GitHub Repsoitory: https://github.com/ItsHex/Twitter-MassUnfollow
