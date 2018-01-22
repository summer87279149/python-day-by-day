#! python3
# coding=utf-8
#每次我在 Google 上搜索时，都不会一次只看一个搜索结果。
#我会在一些新的选项卡中打 开前几个链接，稍后再来查看。
# 我经常搜索 Google，所以这个工作流程(开浏览器， 查找一个主题，依次用中键点击几个链接)变得很乏味。
# 如果我只要在命令行中输 入查找主题，就能让计算机自动打开浏览器，
# 并在新的选项卡中显示前面几项查询 结果，那就太好了
import requests, sys, webbrowser, bs4
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.r a')
numToOpen=min(5,len(linkElems))
for i in range(numToOpen):
    webbrowser.open('http://google.com' +linkElems[i].get('href'))


