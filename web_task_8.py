
import requests
import json
from bs4 import BeautifulSoup
rel=requests.get("https://www.imdb.com/title/tt0066763/")
soup=BeautifulSoup(rel.content,"html.parser")
con=soup.find('script',type='application/ld+json').text
a=json.loads(con)
# print(a)
l={}
for key in a:
    if key=="url":
        s=a[key]
        l['id']=s
    # print(l)
with open("task_8.json","w")as f:
    json.dump(l,f,indent=2)


