a,b,c,d=map(int,input().split())
if (a+b)%2==0 and (c+d)%2==0:
    print('YES')
elif (a+b)%2!=0 and (c+d)%2!=0:
    print('YES')
else:
    print('NO')
