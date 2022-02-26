import tweepy
import keys
from datetime import datetime, timedelta
import math
import settings
import random

def lambda_handler(event, context):

    #### Variables #####
    search_count = 150
    rt_count = 0
    create_count = 0
    list_one= settings.LIST_ONE_ID
    list_two= settings.LIST_TWO_ID

    client = getClient()

    out = client.get_tweet(settings.OWN_TWEET_ID, tweet_fields=['author_id'],expansions=['author_id'] )
    author_id = out.data.author_id


    # number = math.ceil(datetime.now().minute / 15)
    number = 5

    now = datetime.utcnow()
    old1 = now - timedelta(hours=1)
    old4 = now - timedelta(hours=4)

    with open('tweets.txt', 'r') as f:
        tweet_string = f.read()
    tweet_list= tweet_string.split("---")
    random.shuffle(tweet_list)

    live = True # used to turn off, if needed
    if(live):
        if number == 1:
            print("#476 tweets related")
            hashtag476Changes(client,author_id,rt_count,create_count,tweet_list,old4,search_count)
        elif number == 2:
            print("#auspoll related changes")
            hashtagAuspollChanges(client,author_id,rt_count,create_count,tweet_list,old4,search_count)
        elif number == 3:
            print("List one changes")
            listChanges(client,list_one,create_count,tweet_list,old1,search_count)
        elif number == 4:
            print("List two changes")
            listChanges(client,list_two,create_count,tweet_list,old1,search_count)

def getClient():    
    client = tweepy.Client(
        bearer_token=keys.BEARER_TOKEN, 
        consumer_key=keys.API_KEY, 
        consumer_secret=keys.API_SECRET, 
        access_token=keys.ACCESS_TOKEN, 
        access_token_secret=keys.ACCESS_SECRET)
    return client

def hashtag476Changes(client, author_id, rt_count,create_count,tweet_list,old,search_count):
    for tweet in tweepy.Paginator(client.search_recent_tweets, start_time=old, query="#476visa -is:retweet", tweet_fields=['author_id','in_reply_to_user_id','public_metrics'],
                                        expansions=['author_id','entities.mentions.username'], max_results=100).flatten(limit=search_count):
        total_rt = tweet.public_metrics['retweet_count'] + tweet.public_metrics['quote_count']
        if(tweet.in_reply_to_user_id == None and tweet.author_id != author_id ):
            # RT
            if(rt_count < 50):
                try:
                    client.retweet(tweet.data['id'], user_auth=True)  
                    client.like(tweet.data['id'], user_auth=True)
                    rt_count += 1
                except Exception as e:
                    print("Error RT tweet, tweet id -> " +tweet.data['id'] + str(e) )    
            # quote tweet
            if(create_count < len(tweet_list)):
                print(tweet.author_id)
                try:
                    client.create_tweet( quote_tweet_id=tweet.data['id'], text=tweet_list[create_count])
                    create_count += 1
                except Exception as e:
                    print("Error quoting tweet, tweet id -> " + tweet.data['id'] + str(e))
    for i in tweet_list:
        if(create_count<25 and create_count < len(tweet_list)):
            try:
                client.create_tweet( text=tweet_list[create_count])
                create_count += 1
            except Exception as e:
                print("Error creating tweet" + str(e) )    

def hashtagAuspollChanges(client,author_id,rt_count,create_count,tweet_list, old, search_count):
    for tweet in tweepy.Paginator(client.search_recent_tweets, start_time=old, query="#auspoll OR #auspol OR #nswpol OR #auspoll2022 -is:retweet -#476visa", tweet_fields=['author_id','in_reply_to_user_id','public_metrics'],
                                        expansions=['author_id','entities.mentions.username'], max_results=100).flatten(limit=search_count):
        total_rt = tweet.public_metrics['retweet_count'] + tweet.public_metrics['quote_count']
        if(total_rt >= 10 and tweet.author_id != author_id ):
            # RT
            if(rt_count < 50):
                try:  
                    client.like(tweet.data['id'], user_auth=True)
                    rt_count += 1
                except Exception as e:
                    print("Error liking tweet, tweet id -> " +tweet.data['id'] + str(e))    
            # reply tweet
            if(create_count < len(tweet_list)):
                try:
                    client.create_tweet( in_reply_to_tweet_id=tweet.data['id'], text=tweet_list[create_count])
                    create_count += 1
                except Exception as e: 
                    print("Error replying tweet, tweet id -> " +tweet.data['id'] + str(e))
    for i in tweet_list:
        if(create_count<25 and create_count < len(tweet_list)):
            try:
                client.create_tweet( text=tweet_list[create_count])
                create_count += 1
            except Exception as e:
                print("Error creating tweet" + str(e))    

def listChanges(client,list_name,create_count,tweet_list,old, search_count ):
    for tweet in tweepy.Paginator(client.get_list_tweets, id=list_name, tweet_fields=['author_id','in_reply_to_user_id','public_metrics'],
                    expansions=['author_id','entities.mentions.username'], max_results=100).flatten(limit=search_count):
        if(create_count<25 and create_count < len(tweet_list)): 
            try:
                client.create_tweet( in_reply_to_tweet_id=tweet.data['id'], text=tweet_list[create_count])
                create_count += 1
            except Exception as e:
                print("Error replying tweet, tweet id -> " +tweet.data['id'] + str(e) )  
    print("Count->>>"+ create_count)

lambda_handler(None,None)