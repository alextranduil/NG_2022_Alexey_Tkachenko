theLargestNumber = int(input("Enter number for factorial: "))
number = 1
Factorial = number
lineOfNumbers = {number}
while number < theLargestNumber:
    number = number + 1
    lineOfNumbers.add(number)
    Factorial = Factorial *number
print ("Factorial: " +str(Factorial))