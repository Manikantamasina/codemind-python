t=int(input())
for _ in range(t):
    n=int(input())
    m=n
    while True:
        fc=0
        for i in range(1,m+1):
            if m%i==0:
                fc+=1
        if fc==2:
            break
        m+=1
    
    
    a=n
    while True:
        fc=0
        for j in range(1,a+1):
            if a%j==0:
                fc+=1
        if fc==2:
            break
        a-=1
    if n-a<=m-n:
        print(a)
    else:
        print(m)