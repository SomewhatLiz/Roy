import praw
import time
import info

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

def checkBans(banList, author):
    for name in banList:
        if name == author:
            return False
    return True

def printTest(comment):
    print(comment.author)
    print(comment.body)
    print(20*'-')

url = input("Link to stream: ")
sub = reddit.submission(url)
sub.comment_sort = "new"
lastComment = ""
banList = ['PopcornBleach', 'thepenguiofroblox']

sub = reddit.submission(url)
sub.comments.replace_more(limit=10)
comment = comment = sub.comments.list()[len(sub.comments.list()) - 1]
if checkBans(banList, comment.author):
    textToSpeech(comment.body, lastComment)
lastComment = comment.body
comment = sub.comments.list()[len(sub.comments.list()) - 1]

while 10==10:
    sub = reddit.submission(url)
    sub.comments.replace_more(limit=10)
    printTest(comment)
    if checkBans(banList, comment.author):
        textToSpeech(comment.body, lastComment)
        #typeComment(comment.body, lastComment)
    lastComment = comment.body
    comment = sub.comments.list()[len(sub.comments.list()) - 1]
