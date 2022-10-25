
# a=[2,3,4,5,6,7]
# i=0
# j=-1
# b=[]
# while i<len(a)/2:
#     c=a[i]*a[j]
#     # b.append(c)
#     b.append(c%10)
#     i=i+1
#     j=j-1
# print(b)
    




import json
with open('task_5.json',"r") as f:
    j=json.load(f)
    sub={}
    i=0
    num=0
    n=0
    r=0
    while i<len(j):
        if j['language']=="english":
            num=num+1
        if j['language']=='hindi':
            n=n+1
        if j['language']=='malyalam':
            r=r+1
        i=i+1
        sub['english']=num
        sub['hindi']=n
        sub['malyalam']=r
with open("task_6.json","w")as f:
    json.dump(sub,f)
    
    