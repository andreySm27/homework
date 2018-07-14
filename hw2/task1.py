ins = input('\033[1m\033[31mInput int from 10000 to 99999 : ')
try:
	ins = int(ins)
	if ins < 10000 or ins > 99999:
		print('\033[1m\033[31m\033[43m	---ERROR---	\033[0m')
	else:
		ins=str(ins)
		ina=[]
		for x in range(0,5):
			ina.append(ins[x])
			ina[x]=int(ina[x])
		ina.sort()
		print('\033[1m\033[35m\033[47m			'+str(ina[4])+'			\033[0m')
except ValueError:
	print('\033[1m\033[31m\033[43m	---ERROR---	\033[0m')
