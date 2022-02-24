import tweepy;
import keys
from datetime import datetime
import math

# def lambda_handler(event, context):
    
#     return {
#         "statusCode": 200,
#         "body": json.dumps({
#             "message": "hello world",
#             # "location": ip.text.replace("\n", "")
#         }),
#     }

client = tweepy.Client(
    bearer_token=keys.BEARER_TOKEN, 
    consumer_key=keys.API_KEY, 
    consumer_secret=keys.API_SECRET, 
    access_token=keys.ACCESS_TOKEN, 
    access_token_secret=keys.ACCESS_SECRET)

user = client.get_user(username='awesomeharshas')
userTweets = client.get_users_tweets(user.data.id, exclude=['retweets'],expansions=['author_id'])
author_id = userTweets.data[0].author_id
# author_id = '1493982336458784770'

# out = client.create_tweet( in_reply_to_tweet_id="1496816267423977480", text="Wow")
# out = client.like('1496402648525942789' , user_auth=True)
# print(out)
number = math.ceil(datetime.now().minute / 15)

# todo - change to 180
search_count = 20
rt_count = 0
create_count = 0
list_one='1496816500262547458'
list_two='1496816876734849028'

tweet_list=[]


live = False
if(live):
    if number == 1:
        print("1..")
        for tweet in tweepy.Paginator(client.search_recent_tweets, query="#476visa -is:retweet", tweet_fields=['author_id','in_reply_to_user_id','public_metrics'],
                                      expansions=['author_id','entities.mentions.username'], max_results=60).flatten(limit=search_count):
            total_rt = tweet.public_metrics['retweet_count'] + tweet.public_metrics['quote_count']
            if(total_rt >= 5 and tweet.author_id != author_id ):
                # RT
                if(rt_count < 50):
                    client.retweet(tweet.data['id'], user_auth=True)  
                    client.like(tweet.data['id'], user_auth=True)
                    rt_count += 1
                # quote tweet
                client.create_tweet( quote_tweet_id=tweet.data['id'], text="Please restore #476visa expired due to border closure.")
                create_count += 1

        for i in tweet_list:
            if(create_count<200):
                client.create_tweet( text="Please restore #476visa expired due to border closure.")
                create_count += 1

    elif number == 2:
        print("2..")
        for tweet in tweepy.Paginator(client.search_recent_tweets, query="#auspoll OR #auspol OR #nswpol OR #auspoll2022 -is:retweet", tweet_fields=['author_id','in_reply_to_user_id','public_metrics'],
                                      expansions=['author_id','entities.mentions.username'], max_results=60).flatten(limit=search_count):
            total_rt = tweet.public_metrics['retweet_count'] + tweet.public_metrics['quote_count']
            if(total_rt >= 50 and tweet.author_id != author_id ):
                # RT
                if(rt_count < 50):  
                    client.like(tweet.data['id'], user_auth=True)
                    rt_count += 1
                # reply tweet
                client.create_tweet( quote_tweet_id=tweet.data['id'], text="Please restore #476visa expired due to border closure.")
                create_count += 1

        for i in tweet_list:
            if(create_count<200):
                client.create_tweet( in_reply_to_tweet_id=tweet.data['id'], text="Please restore #476visa expired due to border closure.")
                create_count += 1
    elif number == 3:
        print("3..")
        for tweet in tweepy.Paginator(client.get_list_tweets, id=list_one, tweet_fields=['author_id','in_reply_to_user_id','public_metrics'],
                 expansions=['author_id','entities.mentions.username'], max_results=60).flatten(limit=search_count):
            if(create_count<200): 
                client.create_tweet( in_reply_to_tweet_id=tweet.data['id'], text="Please restore #476visa expired due to border closure.")
                create_count += 1
        
        for i in tweet_list:
            if(create_count<200):
                client.create_tweet( in_reply_to_tweet_id=tweet.data['id'], text="Please restore #476visa expired due to border closure.")
                create_count += 1
    elif number == 4:
        print("4..")
        for tweet in tweepy.Paginator(client.get_list_tweets, id=list_two, tweet_fields=['author_id','in_reply_to_user_id','public_metrics'],
                 expansions=['author_id','entities.mentions.username'], max_results=60).flatten(limit=search_count):
            if(create_count<200): 
                client.create_tweet( in_reply_to_tweet_id=tweet.data['id'], text="Please restore #476visa expired due to border closure.")
                create_count += 1
        
        for i in tweet_list:
            if(create_count<200):
                client.create_tweet( in_reply_to_tweet_id=tweet.data['id'], text="Please restore #476visa expired due to border closure.")
                create_count += 1


print(create_count)
