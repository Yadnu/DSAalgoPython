T=int(input())
while(T>0):
    n=(input())
    rev=n[::-1]
    rev=int(rev)
    n=int(n)
    sum=rev%10+n%10
    print(sum)
    
    T-=1
