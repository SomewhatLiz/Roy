import pyttsx3

voice = pyttsx3.init()

volume = voice.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print(volume)                          #printing current volume level
voice.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

def textToSpeech(body, lastComment):
    if lastComment != body:
        voice.say(body)
        voice.runAndWait()
