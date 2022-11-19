from cs50 import get_int

def typeOfCard(listOfCardNumberElements):
    match len(listOfCardNumberElements):
        case 15:
            AmericanExpress(listOfCardNumberElements)
        case 13:
            Visa(listOfCardNumberElements)
        case 16:
            VisaOrMasterCard(listOfCardNumberElements)
        case _:
            print("INVALID")

def AmericanExpress(listOfCardNumberElements):
    match listOfCardNumberElements[0]:
        case 3:
            match listOfCardNumberElements[1]:
                case 4:
                    print("AMEX")
                case 7:
                    print("AMEX")
                case _:
                    print("INVALID")
        case _:
            print("INVALID")

def Visa(listOfCardNumberElements):
    if listOfCardNumberElements[0] == 4:
        print("VISA")
    else:
        print("INVALID")

def VisaOrMasterCard(listOfCardNumberElements):
    match listOfCardNumberElements[0]:
        case 4:
            Visa(listOfCardNumberElements)
        case 5:
            match listOfCardNumberElements[1]:
                case 1:
                    print("MASTERCARD")
                case 2:
                    print("MASTERCARD")
                case 3:
                    print("MASTERCARD") 
                case 4:
                    print("MASTERCARD")   
                case 5:
                    print("MASTERCARD")
                case _:
                    print("INVALID")
        case _:
            print("INVALID")

def Luhn_Algorithm(listOfCardNumberElements):
    reversedListOfCardNumberElements = list(reversed(listOfCardNumberElements))
    index_for_multiply = 1
    listOfMultipliedElements = []
    while index_for_multiply < len(reversedListOfCardNumberElements):
        element_multiply_2 = reversedListOfCardNumberElements[index_for_multiply]*2
        list_of_element_multiply_2 = [int(numeral) for numeral in str(element_multiply_2)]
        listOfMultipliedElements.extend(list_of_element_multiply_2)
        reversedListOfCardNumberElements.pop(index_for_multiply)
        index_for_multiply = index_for_multiply + 1 
    sum_of_multiplied_elements = sum(listOfMultipliedElements)
    sum_of_non_multiplied_elements = sum(reversedListOfCardNumberElements)
    final_sum = sum_of_multiplied_elements + sum_of_non_multiplied_elements
    list_of_final_sum = [int(numeral) for numeral in str(final_sum)]
    if list_of_final_sum[-1] == 0:
        typeOfCard(listOfCardNumberElements)
    else:
        print("INVALID")

cardNumber = get_int("Enter card number: ")
listOfCardNumberElements = [int(numeral) for numeral in str(cardNumber)]

Luhn_Algorithm(listOfCardNumberElements)