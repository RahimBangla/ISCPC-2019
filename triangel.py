n = int(input())  
i = 0
while n > i: 
    inputs= input()
    a = int(inputs.split(" ")[0])
    b = int(inputs.split(" ")[1])
    c = int(inputs.split(" ")[2])
    if (a+b>c and a+c>b and b+c>a):
        s = (a+b+c)/2
        area = (s * (s-a) * (s-b) * (s-c))**0.5
        print(format(area, ".2f"))
    else:
        print("Oh, No!")
    i+=1