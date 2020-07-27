import praw
import time
import pynput
import pyttsx3
import info
import webbrowser

voice = pyttsx3.init()

volume = voice.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print(volume)                          #printing current volume level
voice.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()
reddit = praw.Reddit(client_id = info.getId(),
                     client_secret = info.getSecret(),
                     user_agent = info.getUsername(),
                     username = info.getUsername(),
                     password = info.getPassword())

chrome = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

print('praw version: {}'.format(praw.__version__))

url = input("Link to stream: ")
sub = reddit.submission(url)
sub.comment_sort = "new"
lastComment = ""

sub = reddit.submission(url)
sub.comments.replace_more(limit=0)
comment = sub.comments.list()[len(sub.comments.list()) - 1]
print(comment.body)
time.sleep(1)
voice.say(comment.body)
voice.runAndWait()

def textToSpeech(body, lastComment):
    if lastComment != comment.body:
        voice.say(comment.body)
        voice.runAndWait()

def openLink(body, lastComment):
    if lastComment != comment.body:
        webbrowser.open(comment.body, new=0, autoraise=True)

while 10==10:
    sub = reddit.submission(url)
    sub.comments.replace_more(limit=10)
    print(comment)
    print(comment.body)
    print(20*'-')
    textToSpeech(comment.body, lastComment)
    lastComment = comment.body
    comment = sub.comments.list()[len(sub.comments.list()) - 1]
