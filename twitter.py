from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener


consumer_key="IHO7c3kX9cPXeC5yymwkX7ySF"
consumer_secret="5WxVESOsFbF87KviFjn8S1oROjHrfmOLNMKfH0gbMgNAAkwU69"

access_token = "2241581574-oaHtX7XWAjk2Ljv7TAobCCry3l5sW9ZUrKqGuWf"
access_token_secret = "aDjl7gNSIGIKjwumv2XqGtJXIHsC5WepRwhHVCBG8UKqP"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

import json

tweets = []
class listener(StreamListener):
	def __init__(self, api=None):
		super(listener, self).__init__()
		self.num_tweets = 0

	def on_data(self, data):
		if self.num_tweets < 3:
			d = json.loads(data)
			# print d.get('text')
			tweets.append(d.get('text'))
			self.num_tweets += 1
			print data
			return True
		else:
			return False

	def on_error(self, status):
		print status

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"], languages=["en"])

print tweets

from textblob import TextBlob

#blob = TextBlob()

