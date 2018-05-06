import urllib.request
import lxml.html
# 自己写的第一个爬虫，捂脸，虽然丑的一批，但感觉良好哈哈哈

headers = {'User-agent': 'wswp'}
request = urllib.request.Request('https://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/book?start=0', headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
tree = lxml.html.fromstring(html)
tds = tree.cssselect('div.mod>dl')
for td in tds:
    title = td.cssselect('dd')[0].text_content().strip()
    print(title)
