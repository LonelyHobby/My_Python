import math
a,b,c=input().strip().split()
if a==0:
	print("Wrong")
else:
	delta=pow(b,2)-4*a*c
	x=-b/(2*a)
	if delta==0:
		print x
	elif delta>0:
		x1=x-math.sqrt(delta)/(2*a)
		x2=x+math.sqrt(delta)/(2*a)
		print("x1=%f x2=%f"%(x1,x2))
	else:
		print("No root")
