
# i want only first movie than i use 3 task#

import requests
import json
from bs4 import BeautifulSoup
url_list=[]
with open('task_2.json','r') as f:
    a=json.load(f)
for i in a:
    url_list.append(i['url'])

b=url_list[:10]

details=['name','director','image','description','language','genre',]
l=[]
# print(b)
for j in b:
    rel=requests.get(j)
    soup=BeautifulSoup(rel.content,"html.parser")
    con=soup.find('script',type='application/ld+json').text
    h=json.loads(con)
    dic={}
    for k in h:
        dic['name']=h['name']
        dic['director']=h['director'][0]['name']
        dic['image']=h['image']
        dic['description']=h['description']
        dic["language"]=h['review']['inLanguage']
        dic['genre']=h['genre']
        dic['country']='india'
    l.append(dic)

with open('task_5.json','w') as file:
    json.dump(l,file,indent=8)   