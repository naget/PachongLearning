import urllib.request
import lxml.html
import csv


headers = {'User-agent': 'wswp'}
request = urllib.request.Request('https://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/book?start=0', headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
tree = lxml.html.fromstring(html)
tds = tree.cssselect('div.mod>dl')
# 加个一个导出文件的功能
fields = ('title', 'desc', 'rating_nums')
writer = csv.writer(open('get_douban1-1.csv', 'w'))
writer.writerow(fields)
for td in tds:
    title = td.cssselect('dd>a.title')[0].text_content().strip()
    print(title)
    desc = td.cssselect('dd>div.desc')[0].text_content().strip()
    print(desc)
    rating_nums = td.cssselect('span.rating_nums')[0].text_content().strip()
    print(rating_nums)
    row = [title, desc, rating_nums]
    writer.writerow(row)
