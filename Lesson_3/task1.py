def askForNumbers():
    number = float(input("Enter number: "))
    return number
    
def askForOperating():
    operation = input("Enter one of operations (+, -, *, /): ")
    return operation

def operation(action):
    if action == "+":
        return sum(askForNumbers(), askForNumbers())
    if action == "-":
        return subtraction(askForNumbers(), askForNumbers())
    if action == "*":
        return multiplication(askForNumbers(), askForNumbers())
    if action == "/":
        return division(askForNumbers(), askForNumbers())

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