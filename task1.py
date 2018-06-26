X=input("Must: ");
N=input("Go bed(H): ");
M=input("Go bed(M): ");
time1=N*60+M;
time1=time1+X;
print(time1//60);
print(time1%60);