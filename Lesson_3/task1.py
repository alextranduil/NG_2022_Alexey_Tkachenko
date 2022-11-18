def askForNumbers(text):
    number = float(input(text)) #"Enter number: "))
    return number
    
def askForOperating():
    operation = input("Enter one of operations (+, -, *, /): ")
    return operation

def operation(action):
    match action:
        case "+":
            return sum(askForNumbers(), askForNumbers())
        case "-":
            return subtraction(askForNumbers(), askForNumbers())
        case "*":
            return multiplication(askForNumbers(), askForNumbers())
        case "/":
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