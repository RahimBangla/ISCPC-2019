#include<stdio.h>
#include<math.h>

tc = int(input())
i = 0
ans=0
while tc > i: 
    inputs= input()
    a, r, n = map(int,inputs.split())
    # print(a+(a*r)+(a*r*r))
    i+=1
    while  n > 0:
        ans=ans+(a*pow(r,n-1))
        n-=1
    print(ans)
    ans=0