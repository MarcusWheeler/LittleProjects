import webbrowser
import sys
import os
import signal

#I want to be able to update the url
#I want it to be able to run normally otherwise

if len(sys.argv) > 1: #I must be updating the url if I have an argument
  f = open('C:/Users/Marcus/Documents/url.txt', "w")
  f.write(sys.argv[1])
  sys.exit()
f = open('C:/Users/Marcus/Documents/url.txt', "r")
url = f.read()

# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' #%s has to be added or it doesn't work lmao.

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

webbrowser.get(chrome_path).open(url)

print(url)

os.kill(os.getppid(), signal.SIGTERM)