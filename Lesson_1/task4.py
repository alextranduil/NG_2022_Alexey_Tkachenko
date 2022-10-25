a = float(input("Enter a from the quadratic equation: ")) # a - quadratic coefficient (first coefficient)
b = float(input("Enter b from the quadratic equation: ")) # b - liner coefficient (second coefficient)
c = float(input("Enter c from the quadratic equation: ")) # c - free term
D= b**2 - 4*a*c # D - discriminant
if D>0:
 x1 = -(b-D**0.5)/2*a
 x2 = (b-D**0.5)/2*a # x1, x2 - unknowns
 print ("x1= " + str (x1), "x2= " + str (x2))
if D==0:
 x1= -b/2*a
 x2=x1
 print ("x1=x2= " + str (x1))
if D<0:
 print ("There are no solutions")