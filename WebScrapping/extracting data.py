import bs4 as bs
import urllib.request

url="https://en.wikipedia.org/wiki/Python_(programming_language)"
sause=urllib.request.urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)').read()
soup=bs.BeautifulSoup(sause,'lxml')
soup.prettify()
##print(soup.title.p)
###html.parsor,html5lib,lxml Parsors
##
##for para in soup.find_all('p'):
##      print(para.text[:])
##      print(para.string)
##print(soup.get_text())
##
##for url in soup.find_all('a'):
##      print(url.get('href'))

import os
os.mkdir('wikipedia')

c=0
f=open("w.txt",'w')
for url in soup.find_all('a'):
      if c<20:
            print(url.get('href'))
            f.write("{}".format(url.get('href'))+'\n')
            c+=1
      else:
            break
f.close()

