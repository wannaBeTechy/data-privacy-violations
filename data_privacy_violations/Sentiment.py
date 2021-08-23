# -*- coding: utf-8 -*-
import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
import numpy as np
import json
import pandas as pd
from dateutil.parser import parse
class TwitterClient(object): 
   
    def clean_tweet(self, tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        #import PreProcessing
        #PreProcessing.preProcess(tweet)
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 

    def get_tweet_sentiment(self, tweet): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(self.clean_tweet(tweet)) 
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'

    def get_tweets(self): 
        ''' 
        Main function to fetch tweets and parse them. 
        '''
        # empty list to store parsed tweets 
        tweets = []

        try: 
            # call twitter api to fetch tweets 
            #fetched_tweets = self.api.search(q = query, count = count) 
            tweets_file = open('twitter_data.txt', "r",encoding='cp1252')
            print(tweets_file)
            # parsing tweets one by one 
            for tweet in tweets_file: 
                
                # empty dictionary to store required params of a tweet 
                try:
                    parsed_tweet = {} 
                    
                    tweett = json.loads(tweet)
                    
                    tweet =tweett.get("text")
                    
                    parsed_tweet['text']=tweet
                   
                    dt = parse(tweett.get("user")['created_at'])
                    fc = parse(tweett.get("user")['followers_count'])
                    print(fc)
                    # saving text of tweet 
                    #parsed_tweet['text'] = tweet.text 
                    # saving sentiment of tweet 
                   
                    sen=self.get_tweet_sentiment(tweet) 
                    parsed_tweet['sentiment'] = sen
                    
                    #print(dt.month,dt.year,sen,tweet)
                    # appending parsed tweet to tweets list 
                    if tweett.get("retweet_count")> 0: 
                        # if tweet has retweets, ensure that it is appended only once 
                        if parsed_tweet not in tweets: 
                            tweets.append(parsed_tweet) 
                        else:
                            print('dup')
                    else: 
                        print(dt.month,dt.year,sen,tweet)
                        tweets.append([dt.month,dt.year,sen,tweet]) 
                except:
                    continue
            # return parsed tweets 
           

        except tweepy.TweepError as e: 
            # print error (if any) 
            print("Error : " + str(e)) 
        return tweets    
def main(): 
    # creating object of TwitterClient Class 
    api = TwitterClient() 
    # calling function to get tweets 
    tweets = api.get_tweets() 
   
if __name__ == "__main__": 
    # calling main function 
    main() 

