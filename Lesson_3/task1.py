def askForFirstNumber():
    number1 = float(input("Enter first number: "))
    return number1

def askForSecondNumber():
    number2 = float(input("Enter second number: "))
    return number2

def askForOperating():
    operation = input("Enter one of operations (+, -, *, /): ")
    return operation

def operation(action):
    if action == "+":
        return sum(askForFirstNumber(), askForSecondNumber())
    if action == "-":
        return subtraction(askForFirstNumber(), askForSecondNumber())
    if action == "*":
        return multiplication(askForFirstNumber(), askForSecondNumber())
    if action == "/":
        return division(askForFirstNumber(), askForSecondNumber())

def sum(number1, number2):
    return  number1 + number2

def subtraction(number1, number2):
    return  number1 - number2

def multiplication(number1, number2):
    return  number1 * number2

def division(number1, number2):
    return  number1 / number2

def result():
    print ("Result: " + str(operation(askForOperating())))

result()