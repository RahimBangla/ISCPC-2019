t = int(input())
i = 0
z = 0
while t > i:
    g = input()
    a, r, n = map(int, g.split())
    i += 1
    while n > 0:
        z += (a*r**(n-1))
        n -= 1
    print(z)
    z = 0
