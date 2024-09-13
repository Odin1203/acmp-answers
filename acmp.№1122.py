x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
if x1-x2==1 and y2-y1==1:
    print('YES')
elif x2-x1==1 and y1-y2==1:
    print('YES')
elif x2-x1==1 and y2-y1==1:
    print('YES')
elif x1-x2==1 and y1-y2==1:
    print('YES')
elif x1==x2 and (y1-y2==1 or y2-y1==1):
    print('YES')
elif y1==y2 and (x1-x2==1 or x2-x1==1):
    print('YES')
else:
    print('NO')
