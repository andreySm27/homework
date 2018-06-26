
col=int(input("Count house: "));
price=int(input("Price 1m: "));
dist=int(input("Distance between house(m): "));
def sums(n):
	x=0;
	N=n
	for X in range(0,n-1):
		x=x+n;
	return x/2;
pass;
u=0;

for p in range(2,col+1):
	u=u+sums(p);
pass;

print(u*dist*price);
