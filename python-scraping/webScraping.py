

from __future__ import print_function,division

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


# 创建了一个getTitle 函数，可以返回网页的标题，如果获取网页的时候遇到问题就返回一个None 对象。
# 在getTitle 函数里面，我们像前面那样检查了HTTPError，然后把两行BeautifulSoup 代码封装在一个
# try 语句里面。这两行中的任何一行有问题，AttributeError 都可能被抛出
# 
def getTitle(url):
    try:
        html =urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

def getSiteHTML(url):
    try:
        html =urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title


def main():
    title = getTitle('http://www.google.com')
    if title == None:
        print('Title could not be found!')
    else:
        print(title)
        
if __name__=="__main__":
    main()
    
        
        