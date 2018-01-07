count=0
for i in range(1,100):
  if 0==i%7 and i%11!=0 or 0==1%11 and i%7!=0:
    print(i,end=" ")
