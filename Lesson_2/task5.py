our_list = str(input("Enter numbers: "))
split_our_list = our_list.split(", ")
list_of_numbers = list(map(float, split_our_list))
index = 0
SumOfElementsExceptOfMinAndMax = 0 
max = max(list_of_numbers)
min = min(list_of_numbers)
for index in range(0,len(list_of_numbers)):
    if list_of_numbers[index] != max and list_of_numbers[index] != min:
        SumOfElementsExceptOfMinAndMax = SumOfElementsExceptOfMinAndMax + list_of_numbers[index]
    index = index + 1
print ("Maximum: " + str(max))
print ("Minimum: " + str(min))
print ("Sum of elements except of maximum and minimum: " + str(SumOfElementsExceptOfMinAndMax))