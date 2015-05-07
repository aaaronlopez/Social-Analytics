# Social-Analytics

A Django application that:
* let's you search for a keyword in any number of tweets and displays an analysis of their sentiments.
* let's you search through any number of tweets of a specific user and displays an analysis of their sentiments.

## Usage
### On Heroku
* https://protected-earth-8489.herokuapp.com/
* WARNING: Heroku limits web requests to 30 seconds. Since usually searches with >100 tweets take more than 30 seconds, try to keep the number of tweets you search through <100. However, everything should definitely work on a local server. A solution is in the works.

### Run Locally
1. Clone this repository.
2. Install all [requirements.txt](https://github.com/aaaronlopez/Social-Analytics/blob/master/requirements.txt).
3. Obtain a Twitter Consumer Key (API Key), Consumer Secret (API Secret), Access Token, and Access Token Secret from [Twitter Developers](https://dev.twitter.com/).
4. Go to [config-example.yml](https://github.com/aaaronlopez/Social-Analytics/blob/master/config-example.yml) and change `secret_key`, `consumer_key`, `consumer_secret`, `access_token`, `access_token_secret`. Rename this to config.yml.
	* `secret_key` can be any random 50 character string, use: `django.utils.crypto.get_random_string(50, chars)`
	* You can also just change the secret key variables at the top of [local.py](https://github.com/aaaronlopez/Social-Analytics/blob/master/project/settings/local.py) if you don't want to use a .yml.
6. Run `python manage.py runserver` from the base of this repo. (it will not work without the keys and tokens)

## How it Works
* Uses [Django](https://www.djangoproject.com/) to run on the web.
* Connects to the [Twitter](https://twitter.com/) API using the power of [Tweepy](https://github.com/tweepy/tweepy)!
* Uses [TextBlob](http://textblob.readthedocs.org/en/dev/) to measure the sentiment of the tweets.
* Sends the data from [Tweepy](https://github.com/tweepy/tweepy) to a rich dashboard that utilizes awesome [Bootstrap](http://getbootstrap.com/), [Google Charts](https://developers.google.com/chart/), and more!

## To-Do
* Use RQ worker to handle large tweet searches!
* Add the ability to search through more social media!
* Add more visually stimulating data representation!

## Author
Aaron Lopez, UC Berkeley

## Acknowledgements
* [Django](https://www.djangoproject.com/) for maybe webapps easy!
* [Heroku](https://www.heroku.com/) for a simple deploy!
* [Twitter](https://twitter.com/) for the data!
* [Tweepy](https://github.com/tweepy/tweepy) for a seamless way to connect to Twitter!
* [TextBlob](http://textblob.readthedocs.org/en/dev/) for a quick way to analyze words!
* [Bootstrap](http://getbootstrap.com/) for a simple framework to make beautiful websites!
* [Google Charts](https://developers.google.com/chart/) for the gorgeous charts!
* [Bootstrap-Table](https://github.com/wenzhixin/bootstrap-table) for the neat tables!
* [Virtualenv](https://virtualenv.pypa.io/en/latest/) for the safety of my environment!

