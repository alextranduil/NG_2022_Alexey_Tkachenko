our_list = str(input("Enter numbers: "))
split_our_list = our_list.split(",")
list_of_numbers = list(map(float, split_our_list))
list_of_numbers.sort()
print ("Maximum: " + str(list_of_numbers[-1]))
list_of_numbers.pop(-1)
print ("Minimum: " + str(list_of_numbers[0]))
list_of_numbers.pop(0)
SumOfElementsExceptOfMinAndMax = sum(list_of_numbers)
print ("Sum of elements except of maximum and minimum: " + str(SumOfElementsExceptOfMinAndMax))