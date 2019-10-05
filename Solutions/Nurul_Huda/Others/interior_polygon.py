
def findAngle(n): 
    interiorAngle = float((n - 2) * 180 / n) 
    print("%.6f"%interiorAngle)
n = int(input())  
i = 0
while n > i:
    findAngle(int(input()))
    i+=1

n = int(input())  
i = 0