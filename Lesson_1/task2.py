firstFloatnumber= float(input("Enter first number: "))
secondFloatnumber= float(input("Enter second number: "))
operating= (input("Enter one of operations (+, -, *, /): "))
if operating == "+":
    Sum = firstFloatnumber + secondFloatnumber
    print ("Sum: " + str (Sum))
if operating == "-":
    Difference = firstFloatnumber - secondFloatnumber
    print ("Difference: " + str (Difference))
if operating == "*":
    Product = firstFloatnumber * secondFloatnumber
    print ("Product: " + str (Product))
if operating == "/":
    Fraction = firstFloatnumber / secondFloatnumber
    print ("Fraction: " + str (Fraction))