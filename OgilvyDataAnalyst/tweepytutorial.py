#This example will download your home timeline tweets and print each one
#of their texts to the console.
import tweepy
from tweepy import OAuthHandler


auth=OAuthHandler("vFutoJoPIDaF8O3U3ifJUnrFw",
"Gfy8ykTjnHf7gxj0kkakRWqY9gWhDEd69aHDWewAWP2hsxCv0z")

auth.set_access_token("855588527039422465-BirmEI78Vvugvm44y5cJzNoMjPiF8B8",
"RjZhI9lCoptKipRcKnPV6Uu4mIa4L0CGk9FoBXJ7GJNnB")

api=tweepy.API(auth)
public_tweets=api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

#streaming with tweepy
'''1.Create a class inheriting from StreamListener
2.Using that class create a Stream object
3.Connect to the Twitter API using the Stream.'''
#creating a stream listener
import tweepy
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
#step 2: creating a stream
#need an api to stream
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
#use filter to stream all tweets containing python
#track is an array of search terms to stream 
myStream.filter(track=['python'])
