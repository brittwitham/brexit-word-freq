# Brexit Word Frequencies 🇬🇧

> Takes all the words from recent Tweets featuring #brexit (or any hashtag), counts the number of times they occur, then returns a list of the top 10 keywords and plots them on a time series chart by the hour.

## Overview

![Screenshot](https://github.com/brittwitham/brexit-word-freq/blob/main/screenshot.png)

This app was created in the (seemingly endless) lead-up to the UK leaving the European Union ('brexit'), so discussions on the topic could be tracked by displaying the top words associated with the hashtag. Since 2020, 'coronavirus' has scarcely left the top words, which make for an interesting research project later down the line.

It also tracked the "#cdnpoli" hashtag ahead of the Canadian election to track the kinds of discussions taking place. For example, "cabinet" and "shuffle" spiked in the hour after the Prime Minister changed a number of ministers, so the hope is for future applications to identify and track these kinds of events for research and practical applications.

## Installation

To use this locally, you'll need a Twitter developer account and a MongoDB Atlas database, so be sure to set those up first and come back once you've got the following details:

[MongoDB Atlas](https://www.mongodb.com/cloud/atlas)

- Complete connection string (including username and password)

[Twitter Developer keys](https://developer.twitter.com/en)

- Consumer key
- Consumer secret
- Access token
- Access token secret

After cloning the repository, create & activate a virtual env:

```
python -m venv [env name]
source [env name]/bin/activate
```

**Install requirements:**

`pip install -r requirements.txt`

**Export environment variables** for Mongo & Twitter, or add them to your .bash_profile. [Check out this video if this is new.](https://www.youtube.com/watch?v=5iWhQWVXosU)

```
export CONSUMER_KEY="consumer key"
export CONSUMER_SECRET="consumer key secret"
export ACCESS_TOKEN="access token""
export ACCESS_TOKEN_SECRET="access token secret"
export DATABASE="connection string (inc. user & pass)"
```

**Start collecting data by running**:

`python word_counter.py`

You'll need at least 12 hours of data for the app to run, so you may want to run the script on a cron job overnight.

Once 12 hours of data is collected, run:

`python app.py`

Then head to http://127.0.0.1:8050/ to see the map in action.

## Technologies

- Dash 1.19.0
- NLTK 3.5
- Tweepy 3.10.0
- Pandas 1.2.1
- Pymongo 3.11.2

## Sources

Word counter inspired by [this tutorial,](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/calculate-tweet-word-frequencies-in-python/) Dash app inspired by the [Plotly docs.](https://plotly.com/python/line-charts/#line-chart-in-dash)

## License

MIT

## Contributors

[Brittany Witham](https://github.com/brittwitham)

Pull requests are welcome.
