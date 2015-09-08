from math import sqrt

def squareroot(x):
   ''' Calculate the square root of a positive number '''
   if x >= 0:
      r=sqrt(x)
      print r*r,x
      assert (r*r) == x
      print "Square root is ",r
   else:
      print "Supplied number (",x,") is negative"
            
