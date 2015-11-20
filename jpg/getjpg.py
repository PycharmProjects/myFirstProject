# -*- coding: utf-8 -*-
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'content="(.*?)" href'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

html = getHtml("http://www.baidu.com")
print html
print getImg(html)

s = 'abc'
s = r'abc'
result = re.findall(s,'abcaaabcaabcabcaa')
print result

s = 'top tip tqp twp tep'
res = r't[io]p'
result = re.findall(res,s)
print result

res = r't[^io]p'
result = re.findall(res,s)
print result

res = r't[ioqwe]p$'
result = re.findall(res,s)
print result

r = r'ab{2}d'
print re.findall(r,'abbdbccbcd')

r = r'a[bc]{2}d'
print re.findall(r,'accdbccbcd')

r = r'ab{0,}d'
print re.findall(r,'abbbbd')

r = r'ab{1,}d'
print re.findall(r,'abd')

r = r'ab{0,1}d'
print re.findall(r,'ad')

#正则表达式编译
#固定电话号码
r1 = r'^\d{3,4}-?\d{8}$'
#定义对象
p_tel = re.compile(r1)
print p_tel
print p_tel.findall('010-12345678')

print dir(re)
