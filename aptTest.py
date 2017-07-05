import tweepy
from tweepy import OAuthHandler

consumer_key = 	'zjY0xGcXQ0UO4PYxVWMWPA4pZ'
consumer_secret = 'zIuGe6z17sCKDJBzvphUpPNSEbqOfa9bh0OS4iQys1K62LGVYg'
access_token = '323763455-QOohhwaojJI7Y94qoo5E94EqbeSjK3HNFmXY2OgY'
access_secret = 'aXLEAq2yqKpcmrRHoqgmRnQVDYHk7xf3wjVhvlU9ItVXj'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

datadump = open("dataDump.txt",'a')
datadump.write('test')

tweets = tweepy.Cursor(api.home_timeline).items(10)
for tweet in tweets:
    print tweet.text
    print " "
    datadump.write(str(tweet))

user = api.get_user('joel_sherwin')
print user.screen_name
print user.followers_count
for friend in user.friends():
   print friend.screen_name

for tweet in tweets:
    datadump.write(tweet)

datadump.close()
    
