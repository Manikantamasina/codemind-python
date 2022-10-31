n=int(input())
x=True
while True:
    if n%2==0:
        n=n//2
    elif n%3==0:
        n=n//3
    elif n%5==0:
        n=n//5
    elif n==1:
        break
    else:
        x=False
        break
if x==True:
    print("Ugly Number")
else:
    print("Not Ugly Number")