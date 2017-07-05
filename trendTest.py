from tweepy import Stream
from tweepy.streaming import StreamListener
import tweepy
from tweepy import OAuthHandler
import os
import time

consumer_key = 	'zjY0xGcXQ0UO4PYxVWMWPA4pZ'
consumer_secret = 'zIuGe6z17sCKDJBzvphUpPNSEbqOfa9bh0OS4iQys1K62LGVYg'
access_token = '323763455-QOohhwaojJI7Y94qoo5E94EqbeSjK3HNFmXY2OgY'
access_secret = 'aXLEAq2yqKpcmrRHoqgmRnQVDYHk7xf3wjVhvlU9ItVXj'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

start_time = time.time()
keyword_list = ['warframe']

#Overriding the listener class
class listener(StreamListener):
    def __init__(self,start_time,time_limit=60):
        self.time=start_time
        self.limit=time_limit
        self.tweet_data=[]
    def on_data(self,data):
        saveFile = io.open('raw_tweets.json','a',encoding = 'utf-8')
        while (time.time() - self.time)<self.limit:
            try:
                self.tweet_data.append(data)
                return True
            except BaseException, e:
                print 'failed ondata', str(e)
                time.sleep(5)
                pass

        saveFile - io.open('raw_tweets.json','w',encoding='utf-8')
        saveFile.write(u'[\n')
        saveFile.write(','.join(self.tweet_data))
        saveFile.write(u'\n]')
        saveFile.close()
        exit

    def on_error(self, status):
        print statuses


twitterStream = Stream(auth, listener(start_time, time_limit=20)) #initialize Stream object with a time out limit
twitterStream.filter(track=keyword_list, languages=['en'])  #call the filter method to run the Stream 
