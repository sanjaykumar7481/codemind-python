a=int(input())
dc=0
while(a):
    d=a%10
    dc+=1
    a//=10
if(dc==10):
    print('Valid')
else:
    print('Invalid')