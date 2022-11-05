import twitter_bot_automator
import tweepy
import config


client = tweepy.Client(consumer_key=config.api_key,
                       consumer_secret=config.api_key_secret,
                       access_token=config.access_token,
                       access_token_secret=config.access_token_secret)

start = twitter_bot_automator.Dandd()
character = start.profession()

client.create_tweet(text=character)