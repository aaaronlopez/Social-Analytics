from django.shortcuts import render
from django.conf import settings

from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
from textblob import TextBlob
from collections import Counter
from scipy.stats import mode
from numpy import median, average
import json

#Tweepy Authorization
auth = OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)

def index(request):
    data = {}
    return render(request, 'front.html', data)

def analyze_tweets(request):
	keyword = request.POST.get('keyword')
	tweet_limit = int(request.POST.get('limit'))

	histogram_data = [['Sentiment']]
	pie_data = [['Sentiment', 'Value'], 
				['Neutral', 0],
				['Positive', 0],
				['Negative', 0]]
	sentiments = {}
	tweets = []

	class listener(StreamListener):
		def __init__(self, api=None):
			super(listener, self).__init__()
			self.num_tweets = 0

		def on_data(self, data):
			if self.num_tweets < tweet_limit:
				tweet = json.loads(data)
				id = tweet['id']
				text = tweet['text']
				blob = TextBlob(text)
				histogram_data.append([blob.sentiment.polarity])
				sentiments[id] = blob.sentiment.polarity
				self.num_tweets += 1
				tweets.append({
					'tweet_id':str(tweet['id']),
					'time':tweet['timestamp_ms'], 
					'screen_name':tweet['user']['screen_name'],
					'sentiment':blob.sentiment.polarity,
					'text':tweet['text'],
					})
				if blob.sentiment.polarity == 0:
					pie_data[1][1] += 1
				elif blob.sentiment.polarity > 0:
					pie_data[2][1] += 1
				elif blob.sentiment.polarity < 0:
					pie_data[3][1] += 1
				return True		
			else:
				return False

		def on_error(self, status):
			print status

	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=[keyword], languages=["en"])

	data = {}
	data['keyword'] = keyword
	data['limit'] = tweet_limit
	data['histogram_data'] = histogram_data
	data['pie_data'] = pie_data
	data['tweets'] = json.dumps(tweets)
	data['average'] = average(sentiments.values())
	data['median'] = median(sentiments.values())
	data['mode'] = mode(sentiments.values())[0][0]
	data['min'] = min(sentiments.values())
	data['max'] = max(sentiments.values())
	data['min_tweet_id'] = min(sentiments, key=sentiments.get)
	data['max_tweet_id'] = max(sentiments, key=sentiments.get)

	# import pdb; pdb.set_trace()

	return render(request, 'dashboard.html', data)

