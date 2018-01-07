a,b=input()
for x in range(a,b):
	s=0
	for y in range(1,x):
		if x%y==0:
			s=s+y
	if x==s:
		print x,  
