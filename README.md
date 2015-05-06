# Social-Analytics

A Django application that:
* let's you search for a keyword in any number of tweets and displays an analysis of their sentiments.
* let's you search through any number of tweets of a specific user and displays an analysis of their sentiments.

## Usage
### On Heroku
* https://protected-earth-8489.herokuapp.com/

### Run Locally
1. Clone this repository.
2. Install all [requirements.txt](https://github.com/aaaronlopez/Social-Analytics/blob/master/requirements.txt).
3. Obtain a Twitter Consumer Key (API Key), Consumer Secret (API Secret), Access Token, and Access Token Secret from [Twitter Developers](https://dev.twitter.com/).
4. Go to [config-example.yml](https://github.com/aaaronlopez/Social-Analytics/blob/master/config-example.yml) and change `secret_key`, `consumer_key`, `consumer_secret`, `access_token`, `access_token_secret`. Rename this to config.yml.
	* `secret_key` can be any random 50 character string, use: `django.utils.crypto.get_random_string(50, chars)`
	* You can also just change the secret key variables at the top of [local.py](https://github.com/aaaronlopez/Social-Analytics/blob/master/project/settings/local.py) if you don't want to use a .yml.
6. Run `python manage.py runserver` from the base of this repo. (this will not work unless you do the above steps)

## How it Works
* Uses [Django](https://www.djangoproject.com/) to run on the web.
* Connects to the [Twitter](https://twitter.com/) API using the power of [Tweepy](https://github.com/tweepy/tweepy)!
* Sends the data from [Tweepy](https://github.com/tweepy/tweepy) to a rich dashboard that utilizes awesome [Bootstrap](http://getbootstrap.com/), [Google Charts](https://developers.google.com/chart/), and more!

## To-Do
* Add the ability to search through more social media!
* Add more visually stimulating data representation!

## Author
Aaron Lopez, UC Berkeley

## Acknowledgements
* [Django](https://www.djangoproject.com/)
* [Heroku](https://www.heroku.com/)
* [Twitter](https://twitter.com/)
* [Tweepy](https://github.com/tweepy/tweepy)
* [Bootstrap](http://getbootstrap.com/)
* [Google Charts](https://developers.google.com/chart/)
* [Bootstrap-Table](https://github.com/wenzhixin/bootstrap-table)
* [Virtualenv](https://virtualenv.pypa.io/en/latest/)

