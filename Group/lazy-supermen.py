
t = int(input())
i=0
while t > i:
    g = input()
    h1 = int(g.split()[0])
    h2 = int(g.split()[1])
    d = int(g.split()[2])
    a1=((h1**2)+((d/2)**2))**.5
    a2=((h2**2)+((d/2)**2))**.5
    i+=1
print(a1,a2)
