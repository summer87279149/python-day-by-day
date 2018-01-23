#! python3
# coding=utf-8
# 博客和其他经常更新的网站通常有一个首页，其中有最新的帖子，以及一个“前一篇”按钮，将你带到以前的帖子。
# 然后那个帖子也有一个“前一篇”按钮，以此 类推。这创建了一条线索，从最近的页面，直到该网站的第一个帖子
# 。如果你希望 拷贝该网站的内容，在离线的时候阅读，可以手工导航至每个页面并保存d
import requests,os,bs4
url = 'http://xkcd.com'
os.makedirs('漫画', exist_ok=True)
while not url.endswith("#"):
    print('下载页面 %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)

    comicElem = soup.select("#comic img")
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:'+comicElem[0].get('src')
        # Download the image.
        print('下载图片:%s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Save the image to ./xkcd.
        print('os.path.basename= %s ' % os.path.basename(comicUrl))
        with open(os.path.join('漫画', os.path.basename(comicUrl)), 'wb') as imageFile:
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
