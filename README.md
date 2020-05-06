# Twitter Robot that Automatically Replies to Mentions

A simple twitter bot that responds to mentions with phrases from my favorite employee at Colégio Catarinense: Sanchez.

## Running Your Own Bot

1. First of all, you must have an account with [developer account authorization](https://developer.twitter.com/en/apply-for-access). As soon as you have authorization, Twitter will send you API keys that you need to use this bot.
2. Download/clone all the files in this repository into your machine.
3. Run the following line of code on **terminal** (MacOS, Linux) or **cmd** (Windows) to install [Tweepy](https://www.tweepy.org/) library:  
`pip install tweepy`
4. Change the numbers on lines **4 and 5** (parameters for functions `OAuthHandler` and `set_access_token`) to the API keys you received from Twitter.
5. Change the possible answers on `possible_answers` list (line 21) to the phrases you want your bot to answer.
6. Run the python file (in this case, **sanchez.py**).

## How to Keep the Bot Running
If you want to keep the bot running in the cloud (highly recommended), you can use a site like [PythonAnywhere](https://www.pythonanywhere.com/). This way, the bot will always be running without depending on whether you run on your machine or not.
