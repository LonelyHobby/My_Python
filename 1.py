x=input()
if x>120:
	y=120*80+(x-120)*80*1.15
if x<60:
	y=x*80-700
else:
	y=x*80
print y			
