a=b=1
sum=0
for i in range(1,11):
	c=a+b
	b=a
	a=c
	sum+=(c+0.0)/b
print ("%.6f"%sum)
