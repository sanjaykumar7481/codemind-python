a=int(input())
s=list(map(int,input().split()))
d=[]
l=[]
for i in s:
    if(i%2==0):
        d.append(i)
    else:
        l.append(i)
k=0
c=0
while(k<len(d) and k<len(l)):
    print(d[k],l[k],end=' ')
    c+=2
    k+=1
while(k<len(d)):
    print(d[k],end=' ')
    k+=1
    c+=1
while(k<len(l)):
    print(l[k],end=' ')
    k+=1
    c+=1
if(c%2):
    print('0',end=' ')