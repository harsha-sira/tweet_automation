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

client = tweepy.Client(bearer_token=keys.BEARER_TOKEN, 
consumer_key=keys.API_KEY, 
consumer_secret=keys.API_SECRET, 
access_token=keys.ACCESS_TOKEN, 
access_token_secret=keys.ACCESS_SECRET,wait_on_rate_limit=False)

user = client.get_user(username='harsha_sira')
print(user.data.name)

results = client.search_recent_tweets("#476visa" , expansions= "author_id,attachments.media_keys,entities.mentions.username" , max_results=100)
# 180
count = 0
for tweet in tweepy.Paginator(client.search_recent_tweets, query="#476visa -is:retweet", expansions= "author_id,attachments.media_keys,entities.mentions.username", max_results=10).flatten(limit=20):
    # this if for testing only
    if(count ==0):
        print(tweet)
        # check rt is not by me and number of RT count
        

    
    count +=1

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