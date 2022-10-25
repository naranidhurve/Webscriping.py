
# import json
# from  bs4 import BeautifulSoup
# import requests
# url= "https://www.imdb.com/india/top-rated-indian-movies"
# req=requests.get(url)
# soup=BeautifulSoup(req.text,"html.parser")
# # print(soup)
# def scrap_top_list():
#     main_div=soup.find('div',class_='lister')
#     tbody=main_div.find('tbody',class_='lister-list')
#     trs=tbody.find_all('tr')
#     movie_rank=[]
#     movie_name=[]
#     year_of_release=[]
#     movie_urls=[]
#     movie_rating=[]
#     for tr in trs:
#         position=tr.find('td',class_="titleColumn").get_text().strip()
#         rank=''
#         for i in position:
#             if '.' not in i: 
#                 rank=rank+i
#             else:
#                 break
#         movie_rank.append(rank)
#         title=tr.find('td',class_="titleColumn").a.get_text()
#         movie_name.append(title)
#         year=tr.find('td',class_="titleColumn").span.get_text()
#         year_of_release.append(year)
#         imdb_rating=tr.find('td',class_="ratingColumn").strong.get_text()
#         movie_rating.append(imdb_rating)

#         link=tr.find("td",class_="titleColumn").a["href"]
#         movie_link="https://www.imdb.com"+link
#         top_movies=[]
#         movie_urls.append(movie_link)
#         details={'position':' ','name':' ','year':' ','rating':' ','url':' '}
#         for i in range(0,len(movie_rank)):
#             details['position']=int(movie_rank[i])
#             details['name']=str(movie_name[i])
#             year_of_release[i]=year_of_release[i][1:5]
#             # details['year']=int(year_of_release[i])
#             details['rating']=float(movie_rating[i])
#             details['url']=movie_urls[i]
#             top_movies.append(details.copy())
#         with open("task_11.json","w")as f:
#            json.dump(top_movies,f,indent=4)
#     # return("top_movies")
#         # print(movie_urls)
# scrap_top_list()
    
    
# import requests
# import json
# from bs4 import BeautifulSoup
# with open("task_2.json","r")as f:
#     movie=json.load(f)
#     i=0
#     rel=[]
#     while i<len(movie):
#         print(i+1,":",movie[i]["name"])
#         rel.append(movie[i]["url"])
#         i=i+1
#     movie_num=int(input("enter the number:"))-1
#     b=rel[movie_num]
#     d=requests.get(b)
#     soup=BeautifulSoup(d.content,"html.parser")
#     com=soup.find('script',type='application/ld+json').text
#     a=json.loads(com)
#     dict={}
#     for i in a:
#         dict['name']=a['name']
#         dict['director']=[a['director'][0]['name']]
#         dict['image']=a['image']
#         dict['description']=a['description']
#         dict['language']=a['review']['inLanguage']
#         dict['genre']=a['genre']
#         dict['country']='india'
# with open("task_11.json","w")as f:
#     json.dump(dict,f,indent=8)



import json
with open('task_5.json',"r") as f:
    j=json.load(f)
    sub={}
    i=0
    num=0
    n=0
    r=0
    while i<len(j):
        if j['language']=='English':
            num=num+1
        if j['language']=='hindi':
            n=n+1
        if j['language']=='malyalam':
            r=r+1
        i=i+1
        sub['english']=num
        sub['hindi']=n
        sub['malyalam']=r
with open("task_11.json","w")as f:
    json.dump(sub,f)
    
    