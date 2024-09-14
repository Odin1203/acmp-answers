x,y=map(int,input().split())
if x==1 and y==1:
    print(0)
elif x>1 and y>1 and x==y:
    print(2)
elif x==1 and y>1:
    print(1)
elif y==1 and x>1:
    print(1)
else:
    print(1)
