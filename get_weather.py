#! python3
#
# 下载今后几天的天气预报，并以纯文本打印出来
from pprint import pprint
import json, requests, sys,urllib.parse
if len(sys.argv)<2:
    print('使用方法 get_weather.py 地名')
    sys.exit()
location = ''.join(sys.argv[1:])
location=urllib.parse.quote(location)
url ='http://www.sojson.com/open/api/weather/json.shtml?city=%s' % (location)
response = requests.get(url)
# pprint(vars(response));
response.raise_for_status()
w = json.loads(response.text)
print('当前天气:')
print(w['data']['yesterday']['type'], '-', w['data']['yesterday']['notice'])