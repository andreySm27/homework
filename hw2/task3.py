import random
arrL = random.randint(0,99)
arrRan=[random.randint(0,99) for i in range(arrL)]
try:
	sumArrL=int(input('\033[1m\033[31mInput n (0-'+str(arrL)+'): '))
	sumArr = 0
	for x in range(0,sumArrL):
		sumArr += arrRan[x]
	print('		\033[1m\033[47m\033[30mSum = '+str(sumArr)+'\033[0m')
except ValueError:
	print('\033[1m\033[31m\033[43m	---ERROR---	\033[0m')