t = int(input())
i = 0
z = 0
while t > i:
    g = input()
    a = int(g.split()[0])
    r = int(g.split()[1])
    n = int(g.split()[2])
    i += 1
    while n > 0:
        z += (a*r**(n-1))
        n -= 1
    print(z)
    z = 0
