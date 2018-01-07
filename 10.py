from __future__ import print_function
x=input()
count=1
print ('%d,'%x,end='')
while(x!=1):
        if (0==x%2):
          x=x/2
          count+=1
          if (x!=1):
            print ("%d,"%x,end='')
          else:
            print ("%d"%x,end='')
        else:
          x=x*3+1
          count+=1
          if (x!=1):
            print ("%d,"%x,end='')
          else:
            print ("%d"%x,end='')
print ("\nstep=%d"%count)
