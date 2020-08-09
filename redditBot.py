import praw
import time
import info
import twitter

import tts
import type
import links

reddit = praw.Reddit(client_id = info.getId(),
                     client_secret = info.getSecret(),
                     user_agent = info.getUsername(),
                     username = info.getUsername(),
                     password = info.getPassword())

print('praw version: {}'.format(praw.__version__))

def textToSpeech(body, lastComment):
    tts.textToSpeech(body, lastComment)

def openLink(body, lastComment):
    links.openLink(body, lastComment)

def typeComment(body, lastComment):
    type.checkType(comment, lastComment)

def control(comment, lastComment):
    type.control(comment, lastComment)

def tweet(comment, lastComment):
    twitter.tweet(comment, lastComment)

def checkBans(banList, author):
    for name in banList:
        if name == author:
            return False
    return True

def printTest(comment):
    print(comment.author)
    print(comment.body)
    print(20*'-')

commentRepeats = 0
commentThreshhold = 10

url = input("Link to stream: ")
sub = reddit.submission(url)
sub.comment_sort = "new"
lastComment = ""
banList = ['PopcornBleach', 'thepenguiofroblox', 'Clown_Unknown', 'Munchlax-Gamer']

sub = reddit.submission(url)
sub.comments.replace_more(limit=10)
comment = sub.comments.list()[len(sub.comments.list()) - 1]
if checkBans(banList, comment.author):
    textToSpeech(comment.body, lastComment)
lastComment = comment.body
comment = sub.comments.list()[len(sub.comments.list()) - 1]

while 10==10:
    print(commentRepeats)
    sub = reddit.submission(url)
    sub.comments.replace_more(limit=10)
    printTest(comment)
    if checkBans(banList, comment.author):
        if comment.body[:6] != "!https":
            textToSpeech(comment.body, lastComment)
        else:
            #openLink(comment.body[1:], lastComment[1:])
            pass
        if comment.body != lastComment and not command:
            commentRepeats += 1
        command = False
    if commentRepeats >= commentThreshhold:
        commentRepeats = 0
        tweet(comment.body, lastComment)
    lastComment = comment.body
    comment = sub.comments.list()[len(sub.comments.list()) - 1]
