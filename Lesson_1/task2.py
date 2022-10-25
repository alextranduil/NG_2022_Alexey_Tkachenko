from tokenize import Floatnumber

firstFloatNumber = float(input("Enter first number: "))
secondFloatNumber = float(input("Enter second number: "))
Sigh = (input("Enter arithmetic operation (+, -, *, /): "))
if Sigh == "+":
 print ("Sum:" + str(firstFloatNumber + secondFloatNumber))
if Sigh == "-":
 print ("Difference:" + str(firstFloatNumber - secondFloatNumber))
if Sigh == "*":
 print ("Product:" + str(firstFloatNumber * secondFloatNumber))
if Sigh == "/":
 print ("Part:" + str(firstFloatNumber / secondFloatNumber))