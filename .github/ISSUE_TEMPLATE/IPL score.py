from bs4 import BeautifulSoup
import urllib.request
score_page="http://static.cricinfo.com/rss/livescores.xml"
page=urllib.request.urlopen(score_page)
soup=BeautifulSoup(page,'html.parser')
result=soup.find_all('description')

ls=[]
for match in result:
    ls.append(match.get_text())
print(ls)
