
import requests
import json
from bs4 import BeautifulSoup
with open("task_2.json","r")as f:
    movie=json.load(f)
    i=0
    rel=[]
    while i<len(movie):
        print(i+1,":",movie[i]["name"])
        rel.append(movie[i]["url"])
        i=i+1
    movie_num=int(input("enter the number:"))-1
    b=rel[movie_num]
    d=requests.get(b)
    soup=BeautifulSoup(d.content,"html.parser")
    com=soup.find('script',type='application/ld+json').text
    a=json.loads(com)
    dict={}
    for i in a:
        dict['name']=a['name']
        dict['director']=[a['director'][0]['name']]
        dict['image']=a['image']
        dict['description']=a['description']
        dict['language']=a['review']['inLanguage']
        dict['genre']=a['genre']
        dict['country']='india'
with open("task_4.json","w")as f:
    json.dump(dict,f,indent=8)



