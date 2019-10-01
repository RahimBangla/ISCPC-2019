n = int(input())  
i = 0
while n > i: 
    inputs= input()
    aa = inputs.split(" ")[0]
    ab = inputs.split(" ")[1]

    ba = inputs.split(" ")[2]
    bb = inputs.split(" ")[3]
    if (aa == ba or aa == bb or ab == ba or ab == bb):
        print("Possible")
    else:
        print("Oh no!, such a shame")
    i+=1