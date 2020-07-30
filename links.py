import webbrowser
import os

browserExe = "chrome.exe"

chromeLoc = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser(chromeLoc))

def openLink(body, lastComment):
    if lastComment != comment.body:
        os.system("taskkill /f /im "+browserExe)
        webbrowser.get('chrome').open_new_tab(comment.body)
