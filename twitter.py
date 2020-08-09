import info
from twython import Twython
from emoji import UNICODE_EMOJI

consumer_key = info.twitter_key
consumer_secret = info.twitter_secret

access_token = info.twitter_token
access_token_secret = info.twitter_token_secret

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def is_emoji(s):
    count = 0
    for emoji in UNICODE_EMOJI:
        count += s.count(emoji)
        if count > 1:
            return False
    return True

def shorten(comment):
    chars = []
    for char in comment:
        chars.append(char)
    while len(chars) > 280:
        chars.pop(-1)
    returnTweet = ""
    for char in chars:
        if is_emoji(char):
            returnTweet += char
    print(len(returnTweet))
    return returnTweet

def tweet(comment, lastComment):
    if comment != lastComment:
        newComment = shorten("Roy's Thoughts: " + comment)
        twitter.update_status(status=newComment)
        print("Tweeted: %s" % newComment)
