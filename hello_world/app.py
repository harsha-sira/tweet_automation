from http import client
from pydoc import cli
import tweepy;
import keys
from datetime import datetime, timedelta
import math
import json
import settings

def lambda_handler(event, context):

    #### Variables #####
    search_count = 180
    rt_count = 0
    create_count = 0
    list_one= settings.LIST_ONE_ID
    list_two= settings.LIST_TWO_ID

    client = getClient()

    user = client.get_user(username=settings.USERNAME)
    userTweets = client.get_users_tweets(user.data.id, exclude=['retweets'],expansions=['author_id'])
    author_id = userTweets.data[0].author_id

    number = math.ceil(datetime.now().minute / 15)
    # number = 1

    now = datetime.utcnow()
    old = now - timedelta(hours=1)

    with open('tweets.txt', 'r') as f:
        tweet_string = f.read()
    tweet_list= tweet_string.split("---")

    live = False # used to turn off, if needed
    if(live):
        if number == 1:
            print("#476 tweets related")
            hashtag476Changes(author_id,rt_count,create_count,tweet_list,old,search_count)
        elif number == 2:
            print("#auspoll related changes")
            hashtagAuspollChanges(author_id,rt_count,create_count,tweet_list,old,search_count)
        elif number == 3:
            print("List one changes")
            listChanges(list_one,create_count,tweet_list,old,search_count)
        elif number == 4:
            print("List two changes")
            listChanges(list_two,create_count,tweet_list,old,search_count)

def getClient():    
    client = tweepy.Client(
        bearer_token=keys.BEARER_TOKEN, 
        consumer_key=keys.API_KEY, 
        consumer_secret=keys.API_SECRET, 
        access_token=keys.ACCESS_TOKEN, 
        access_token_secret=keys.ACCESS_SECRET)
    return client

def hashtag476Changes(author_id, rt_count,create_count,tweet_list,old,search_count):
    for tweet in tweepy.Paginator(client.search_recent_tweets, start_time=old, query="#476visa -is:retweet", tweet_fields=['author_id','in_reply_to_user_id','public_metrics'],
                                        expansions=['author_id','entities.mentions.username'], max_results=100).flatten(limit=search_count):
        total_rt = tweet.public_metrics['retweet_count'] + tweet.public_metrics['quote_count']
        if(total_rt >= 5 and tweet.author_id != author_id ):
            # RT
            if(rt_count < 50):
                client.retweet(tweet.data['id'], user_auth=True)  
                client.like(tweet.data['id'], user_auth=True)
                rt_count += 1
            # quote tweet
            if(create_count < len(tweet_list)):
                client.create_tweet( quote_tweet_id=tweet.data['id'], text=tweet_list[create_count])
                create_count += 1

        for i in tweet_list:
            if(create_count<25 and create_count < len(tweet_list)):
                client.create_tweet( text=tweet_list[create_count])
                create_count += 1

def hashtagAuspollChanges(author_id,rt_count,create_count,tweet_list, old, search_count):
    for tweet in tweepy.Paginator(client.search_recent_tweets, start_time=old, query="#auspoll OR #auspol OR #nswpol OR #auspoll2022 -is:retweet", tweet_fields=['author_id','in_reply_to_user_id','public_metrics'],
                                        expansions=['author_id','entities.mentions.username'], max_results=100).flatten(limit=search_count):
        total_rt = tweet.public_metrics['retweet_count'] + tweet.public_metrics['quote_count']
        if(total_rt >= 50 and tweet.author_id != author_id ):
            # RT
            if(rt_count < 50):  
                client.like(tweet.data['id'], user_auth=True)
                rt_count += 1
            # reply tweet
            if(create_count < len(tweet_list)):
                client.create_tweet( quote_tweet_id=tweet.data['id'], text=tweet_list[create_count])
                create_count += 1

        for i in tweet_list:
            if(create_count<25 and create_count < len(tweet_list)):
                client.create_tweet( in_reply_to_tweet_id=tweet.data['id'], text=tweet_list[create_count])
                create_count += 1

def listChanges(list_name,create_count,tweet_list,old, search_count ):
    for tweet in tweepy.Paginator(client.get_list_tweets, start_time=old, id=list_name, tweet_fields=['author_id','in_reply_to_user_id','public_metrics'],
                    expansions=['author_id','entities.mentions.username'], max_results=100).flatten(limit=search_count):
        if(create_count<200 and create_count < len(tweet_list)): 
            client.create_tweet( in_reply_to_tweet_id=tweet.data['id'], text=tweet_list[create_count])
            create_count += 1
            
    for i in tweet_list:
        if(create_count<25 and create_count < len(tweet_list)):
            client.create_tweet( in_reply_to_tweet_id=tweet.data['id'], text=tweet_list[create_count])
            create_count += 1
