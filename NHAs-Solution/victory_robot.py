n = int(input())  
i = 0
while n > i:
	inpt = abs(int(input()))
	if inpt == 1971:
		print('Joy Bangla')
	elif (inpt%2) == 0:
		print('Bangla')
	else:
		print('Joy')
	i +=1

