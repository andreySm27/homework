arr=[]
for x in range(0,4):
	arrA=[]
	for x1 in range(1,5):
		arrA.append(x*4+x1)
	arr.append(arrA)
for x in range(0,4):
	for x1 in range(0,4):
		if arr[x][x1]%2==0:
			arr[x][x1]=-1
for x in range(0,4):
	print('\n\033[47m            \033[0m')
	for x1 in range(0,4):
		if arr[x][x1] != -1 and arr[x][x1]<10:
			strS='0'+str(arr[x][x1])
		elif arr[x][x1]>=10:
			strS=str(arr[x][x1])
		print('\033[47m\033[1m\033[31m'+strS,end='\033[47m \033[0m')
		strS='-1'
print('\n\033[47m            \033[0m')
