#! python3
# coding=utf-8
#将拷贝到剪贴板，并在 Google 地图上打开它.

import webbrowser,sys,pyperclip,urllib.parse
if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()
url=address
url=urllib.parse.quote(url)
print(url)
webbrowser.open('https://www.google.com/maps/place/' + url)