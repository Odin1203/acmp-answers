x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
a1=x1-x2
a2=x2-x1
b1=y1-y2
b2=y2-y1

if a1==b1 or a2==b2 or a2==b1 or a1==b2 or x1==x2 or y1==y2:
    print('YES')
else:
    print('NO')
