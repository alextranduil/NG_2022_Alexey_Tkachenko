from rich.console import Console

def countEachElementInString(string_1):
    seted_string = set(string_1)
    result = {}
    for element in seted_string:
        result[element] = string_1.count(element)
    return result

def sortString(string_1):
    sorted_string = ''.join(sorted(string_1))
    return sorted_string

def splitString(string_1):
    splited_string = string_1.split(" ")
    return splited_string

def reversedString(string_1):
    reversed_splited_string = list(reversed(splitString(string_1)))
    return reversed_splited_string

def outputOnlyVowelsOrConsonants(string_1):
    vowels_or_consonats = input("Choose vowels or consonants (v/c): ")
    vowels = "eyuioa"
    consonants = "qwrtpsdfghjklzxcvbnm"
    result = ""
    if vowels_or_consonats == 'v':
        for element in string_1:
            if element in vowels:
                result = result + element
    if vowels_or_consonats == 'c':
        for element in string_1:
            if element in consonants:
                result = result + element
    return result

def wordsByNumbers(string_1):
    index = int(input("Enter index of word: "))
    if index < len(splitString(string_1)): 
        words = splitString(string_1)[index]
        return words
    else:
        print ("Error: index out of range")


def showMenu():
    console.rule("[red] Menu")
    for option in options:
        print("(" + str(options.index(option)) + ")" + " " + option)

def startProgram(string):
    showMenu()
    string_1 = string
    while True:
        choice = int(input("What whould you like to do with your text? "))
        match choice:
            case 0:
                print(sortString(string_1))
            case 1:
                print(countEachElementInString(string_1))
            case 2:
                print(outputOnlyVowelsOrConsonants(string_1))
            case 3:
                print(reversedString(string_1))
            case 4:
                print(wordsByNumbers(string_1))
            case 5:
                string_1 = input("Enter new string: ")
            case 6:
                break
            case _:
                print("Number out of range. Please, choose another one")
    return string_1

string = input("Enter string: ")
console = Console()
options = ("Sort the text", "Count the number of elements", "Output only vowels or consonants", "Split by words and output words from the end", "Output the word by number", "Enter new string", "Close the program")

startProgram(string)