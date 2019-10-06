#Question_link: https://toph.co/p/homework?statement=bn_bd

t = int(input())
i=0
while t > i:
	a=int(input())
	while isinstance((a**0.5), float):
		if len(a) == "":
			break
		else:
			a = int(str(a)[:-1])
			print(a)
	
	i=i+1

# result: still working...........