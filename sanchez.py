import random
import tweepy
from time import sleep

auth = tweepy.OAuthHandler(1, 2)  # API keys you get from twitter
auth.set_access_token(3, 4)
                      
api = tweepy.API(auth, wait_on_rate_limit=True)


def read_last_seen_id():
    with open('last_seen_id.txt', 'r') as f:
        return int(f.read().strip())


def store_last_seen_id(id):
    with open('last_seen_id.txt', 'w') as f:
        f.write(str(id))


possible_answers = ['insert what answers you want here', 'answer2', 'etc']


while True:
    id = read_last_seen_id()
    mentions = api.mentions_timeline(id, tweet_mode='extended')
    try:
        store_last_seen_id(mentions[len(mentions) - 1].id)
    except IndexError:
        pass
    for mention in mentions:
        while True:
            print(f"\nfound {mention.full_text} {mention.id}")
            try:
                api.update_status(f"@{mention.user.screen_name} {possible_answers[random.randint(0, len(possible_answers) - 1)]}",
                              mention.id)
            except tweepy.TweepError:
                print("error, trying again")
                continue
            else:
                print("replied\n")
                break
        sleep(10)
    sleep(20)
