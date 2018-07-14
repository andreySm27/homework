import random
import copy
n=random.randint(4,30)
pole=[['.' for x in range(n)] for a in range(n)]
def draw():
	for x in range(0,n):
		print('')
		for x1 in range(0,n):
			print('\033[47m\033[1m\033[31m'+str(pole[x][x1]),end='\033[0m')
	print('')

pauk=[random.randint(0,n-1),random.randint(0,n-1)]
muxa=[random.randint(0,n-1),random.randint(0,n-1)]
while pauk[1] == muxa[1] and pauk[0] == muxa[0]:
	muxa=[random.randint(0,n-1),random.randint(0,n-1)]
point=copy.copy(pauk)
pole[pauk[1]][pauk[0]]='P'
pole[muxa[1]][muxa[0]]='M'
while muxa[1]!=point[1] and muxa[0]!=point[0]:
	if muxa[1] > point[1] and muxa[0] > point[0]:
		point[1]+=1
		point[0]+=1
		pole[point[1]][point[0]]='\\'
	elif muxa[1] < point[1] and muxa[0] > point[0]:
		point[1]-=1
		point[0]+=1
		pole[point[1]][point[0]]='/'
	elif muxa[1] > point[1] and muxa[0] < point[0]:
		point[1]+=1
		point[0]-=1
		pole[point[1]][point[0]]='/'
	elif muxa[1] < point[1] and muxa[0] < point[0]:
		point[1]-=1
		point[0]-=1
		pole[point[1]][point[0]]='\\'

while muxa[1]!=point[1]:
	if muxa[1] > point[1]:
		point[1]+=1
	elif muxa[1] < point[1]:
		point[1]-=1
	pole[point[1]][point[0]]='|'
while muxa[0]!=point[0]:
	if muxa[0] > point[0]:
		point[0]+=1
	elif muxa[0] < point[0]:
		point[0]-=1
	pole[point[1]][point[0]]='-'
pole[pauk[1]][pauk[0]]='P'
pole[muxa[1]][muxa[0]]='M'
draw()