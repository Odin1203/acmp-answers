n,m=map(str, input().split())
x1=ord(n[0])
y1=ord(n[1])
x2=ord(m[0])
y2=ord(m[1])
a=abs(x1-x2)
b=abs(y1-y2)
s=0
if ((x1==x2 or y1==y2) and (a==1 or b==1)) or (a==b and (a==1 and b==1)):
    print('King')
    s=s+1
if (x1==x2 or y1==y2) or a==b:
    print('Queen')
    s=s+1
if x1==x2 or y1==y2:
    print('Rook')
    s=s+1
if a==b:
    print('Bishop')
    s=s+1
if (a==1 and b==2) or (a==2 and b==1):
    print('Knight')
    s=s+1
if (y1==50 and x1==x2 and (y1-y2==-1 or y1-y2==-2)) or (y1!=49 and x1==x2 and y1-y2==-1):
    print('Pawn')
    s=s+1
if s==0:
    print('Nobody')    
