import os
import tweepy;
import keys

# def lambda_handler(event, context):
    
#     return {
#         "statusCode": 200,
#         "body": json.dumps({
#             "message": "hello world",
#             # "location": ip.text.replace("\n", "")
#         }),
#     }


# api_key = os.environ.get('api_key');
# api_secret= os.environ.get('api_secret')
# access_token= os.environ.get('access_token')
# access_token_secret= os.environ.get('access_token_secret')


auth = tweepy.OAuthHandler(keys.API_KEY, keys.API_SECRET)
auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_SECRET)

# client = tweepy.Client(bearer_token=keys.BEARER_TOKEN ,wait_on_rate_limit=False)

client = tweepy.Client(
    bearer_token=keys.BEARER_TOKEN, 
    consumer_key=keys.API_KEY, 
    consumer_secret=keys.API_SECRET, 
    access_token=keys.ACCESS_TOKEN, 
    access_token_secret=keys.ACCESS_SECRET)

user = client.get_user(username='awesomeharshas')
userTweets = client.get_users_tweets(user.data.id, exclude=['retweets'],expansions=['author_id'])
author_id = userTweets.data[0].author_id

# out = client.create_tweet(text="Please restore #476visa expired due to border closure. \n@ScottMorrisonMP @AlexHawkeMP")
out = client.retweet('1496402648525942789' , user_auth=True)
print(out)

# 180
count = 0
# for tweet in tweepy.Paginator(client.search_recent_tweets, query="#476visa -is:retweet", max_results=10).flatten(limit=20):
# for tweet in tweepy.Paginator(client.search_recent_tweets, query="#476visa -is:retweet", tweet_fields=['author_id','in_reply_to_user_id','public_metrics'],
#                                      user_fields='profile_image_url', expansions=['author_id','entities.mentions.username'], max_results=10).flatten(limit=20):
#  '576309961'
# 1493982336458784770
    # this if for testing only
    # if(count ==7):
        # print(tweet.in_reply_to_user_id)
        # print(tweet.author_id)
        # print(tweet.public_metrics['retweet_count'])
        # print(tweet)
    # total_rt = tweet.public_metrics['retweet_count'] + tweet.public_metrics['quote_count']
    # if(total_rt >= 10 and tweet.author_id != author_id ):
    #     print('found')
    #     print(tweet.data['id'])
        # RT
        # try:
#         client1 = tweepy.Client(bearer_token=keys.BEARER_TOKEN, 
# consumer_key=keys.API_KEY, 
# consumer_secret=keys.API_SECRET, 
# access_token=keys.ACCESS_TOKEN, 
# access_token_secret=keys.ACCESS_SECRET,wait_on_rate_limit=True)
       
        # except:
        #     print('error----->>')            

        

    
    # count +=1

print(count)
# tweepy.Paginator()
# print(len(results.data))
# print(results)

#search for 476`, then RT , Quote tweet mentioning people auspol tag 

# reply to set of offcial account tweets 

# auspol tweets reply


# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)