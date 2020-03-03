#! usr/bin/env python3
#lucky.py - Open several Google search results

import requests,sys,webbrowser,bs4

print('Googling...') #display text while downlading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,features='lxml')
#print(res.text)
#TODO: Open a browser tab for each result.
#linkElems = soup.select('.r')
linkElems = soup.select('div#main > div > div > div > a')
print(linkElems)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com'+ linkElems[i].get('href'))
print(sys.argv[1:])
#程序要做的事
#从命令行参数中获取查询关键字
#取得查询结果页面
#为每个结果打开一个浏览器选项卡

#代码要完成的工作
#从 sys.argv读取命令行参数
#用 requests 模块取得查询结果页面
#找到每个查询结果的链接
#调用 webbrowser.open()函数打开 web 浏览器
