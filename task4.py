Number=input("Number bilet: ");
num1=Number//1000;
num2=Number%1000;
sum1=num1//100+num1%10+(num1%100)//10;
sum2=num2//100+num2%10+(num2%100)//10;
if sum1==sum2:
	print("Good");
	pass
else:
	print("Bad");
	pass