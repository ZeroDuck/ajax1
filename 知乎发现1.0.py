import requests
from pyquery import PyQuery as pq

url = 'https://weibo.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362 '
}
html = requests.get(url,headers=headers).text
doc = pq(html)
print(doc,'\n','\n')
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    print(question)