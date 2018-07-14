import random
rInt = random.randint(1,10)
def isInt(strInt):
	try:
		return int(strInt)
	except ValueError:
		print('\033[1m\033[31m\033[43m	---ERROR---	\033[0m')
for x in range(1,4):
	uInp = input('\033[1m\033[31mYou think my number is : ')
	uInp = isInt(uInp)
	if uInp == rInt:
		print('\033[1m\033[47m\033[30m		You win!		\033[0m')
		break
	elif uInp < rInt:
		print('\033[1m\033[31m\033[43m		Sorry by this number is less than my number		\033[0m')
	elif uInp > rInt:
		print('\033[1m\033[31m\033[43m		Sorry by this number is more than my number		\033[0m')
print('			\033[1m\033[47m\033[30mNumber is '+str(rInt)+'\033[0m')