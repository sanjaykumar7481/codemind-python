a=int(input())
s=list(map(int,input().split()))
d=[]
for i in s :
    if i not in d:
        d.append(i)
print(*d)