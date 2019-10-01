i=int(input());
list1=[]
list2=[]
while i>0:
	x,y=map(int,input().split())
	list1.append(x)
	list2.append(y)
	i-=1
result = []
item = len(list1)
for i in range(item):
    result.append(list1[i]/list2[i])
counter=0
n=0
while len(result)>=n:
	if (result[n]==result[n+1]):
		counter+=1
		n+=1
	else:
		break
print(counter+1)
