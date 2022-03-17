# cpjourney
t=int(input())
while t!=0:
    n=int(input())
    s=c=0
    while c<=n:
        s+=(n-c)**2
        c+=2
    print(s)
    t-=1
