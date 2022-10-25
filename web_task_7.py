
import json
with open('task_5.json','r') as f:
    a=json.load(f)
d={}
for i in a:
    if i['director'] in d:
        d[i['director']]+=1
    else:
        d[i['director']]=1
        # i=i+1
with open("task_7.json","w")as f:
    json.dump(d,f,indent=2)

