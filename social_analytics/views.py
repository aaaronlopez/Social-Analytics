from django.shortcuts import render
from django.conf import settings

from tweepy import OAuthHandler, Stream, API, error
from tweepy.streaming import StreamListener
from textblob import TextBlob
from collections import Counter
from numpy import median, average, std
import json

#Tweepy Authorization
auth = OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)

def index(request):
    return render(request, 'front.html', {'username_error': 'false', 'keyword_error': 'false'})

def analyze_tweets(request):
    selection = request.POST.get('key-selector')
    if selection == "by Keyword":
        return tweets_by_key(request)
    elif selection == "by User":
        return tweets_by_user(request)

def tweets_by_key(request):
    keyword = request.POST.get('key')
    limit = int(request.POST.get('limit'))

    histogram_data = [['Sentiment']]
    pie_chart = [['Sentiment', 'Value'], 
                ['Neutral', 0],
                ['Positive', 0],
                ['Negative', 0]]
    statistics = {}
    tweets = []

    #Twitter Stream
    class listener(StreamListener):
        def __init__(self, api=None):
            super(listener, self).__init__()
            self.num_tweets = 1

        def on_data(self, data):
            if self.num_tweets <= limit:
                tweet = json.loads(data)
                id = tweet['id']
                text = tweet['text']
                favorite_count = tweet['favorite_count']
                retweet_count = tweet['retweet_count']
                blob = TextBlob(text)
                sentiment = blob.sentiment.polarity
                
                #Histogram
                histogram_data.append([blob.sentiment.polarity])

                #Statistics
                statistics[id] = sentiment
                
                #Table
                tweets.append({
                    'screen_name': '<a href="https://twitter.com/' + tweet['user']['screen_name'] 
                                    + '"target="_blank">' + tweet['user']['screen_name'] + '</a>',
                    'sentiment': float("{0:.2f}".format(sentiment)),
                    'text': text + ' <a href="https://twitter.com/statuses/' + 
                                    str(tweet['id']) + '"target="_blank">View</a>',
                    'favorite_count': favorite_count,
                    'retweet_count': retweet_count
                    })

                #Piechart
                if sentiment == 0:
                    pie_chart[1][1] += 1
                elif sentiment > 0:
                    pie_chart[2][1] += 1
                elif sentiment < 0:
                    pie_chart[3][1] += 1

                self.num_tweets += 1
                return True     
            else:
                return False

        def on_error(self, status):
            return render(request, 'front.html', {'username_error': 'false', 'keyword_error': 'true'})

    #Call Twitter Stream
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=[keyword], languages=["en"])

    #Context Data
    data = {
        'keyword': keyword,
        'limit': limit,
        'histogram_data': histogram_data,
        'pie_chart': pie_chart,
        'tweets': json.dumps(tweets),
        'average': float("{0:.5f}".format(average(statistics.values()))),
        'median': float("{0:.5f}".format(median(statistics.values()))),
        'std': float("{0:.5f}".format(std(statistics.values()))),
        'min': float("{0:.5f}".format(min(statistics.values()))),
        'max': float("{0:.5f}".format(max(statistics.values()))),
        'min_tweet_id': min(statistics, key=statistics.get),
        'max_tweet_id': max(statistics, key=statistics.get),
    }
    return render(request, 'dashboard-keyword.html', data)

def tweets_by_user(request):
    user = request.POST.get('key')
    limit = int(request.POST.get('limit'))

    histogram_data = [['Sentiment']]
    pie_chart = [['Sentiment', 'Value'], 
                ['Neutral', 0],
                ['Positive', 0],
                ['Negative', 0]]
    statistics = {}
    tweets = []

    #Twitter Data
    api = API(auth)

    try:
        tweet_data = api.user_timeline(screen_name = user, count=limit, include_rts=False, exclude_replies=True)
    except error.TweepError:
        return render(request, 'front.html', {'username_error': 'true', 'keyword_error': 'false'})

    for tweet in tweet_data:
        text = tweet.text
        id = tweet.id
        favorite_count = tweet.favorite_count
        retweet_count = tweet.retweet_count
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        
        #Histogram
        histogram_data.append([blob.sentiment.polarity])

        #Statistics
        statistics[id] = sentiment
        
        #Table
        tweets.append({
            'sentiment': float("{0:.2f}".format(sentiment)),
            'text': text + ' <a href="https://twitter.com/statuses/' + 
                            str(tweet.id) + '"target="_blank">View</a>',
            'favorite_count': favorite_count,
            'retweet_count': retweet_count
            })

        #Piechart
        if sentiment == 0:
            pie_chart[1][1] += 1
        elif sentiment > 0:
            pie_chart[2][1] += 1
        elif sentiment < 0:
            pie_chart[3][1] += 1

    #Context Data
    data = {
        'user': user,
        'limit': len(tweets),
        'histogram_data': histogram_data,
        'pie_chart': pie_chart,
        'tweets': json.dumps(tweets),
        'average': float("{0:.5f}".format(average(statistics.values()))),
        'median': float("{0:.5f}".format(median(statistics.values()))),
        'std': float("{0:.5f}".format(std(statistics.values()))),
        'min': float("{0:.5f}".format(min(statistics.values()))),
        'max': float("{0:.5f}".format(max(statistics.values()))),
        'min_tweet_id': min(statistics, key=statistics.get),
        'max_tweet_id': max(statistics, key=statistics.get),
    }
    return render(request, 'dashboard-user.html', data)

