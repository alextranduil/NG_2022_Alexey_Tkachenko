our_list = str(input("Enter numbers: "))
split_our_list = our_list.split(", ")
list_of_numbers = list(map(float, split_our_list))
index1 = 1
index0 = 0
max = list_of_numbers[0]
min = list_of_numbers[0]
SumOfElementsExceptOfMinAndMax = 0 
for index1 in range(0,len(list_of_numbers)):
    if list_of_numbers[index1] > max:
        max = list_of_numbers[index1]
    elif list_of_numbers[index1] < min:
        min = list_of_numbers[index1]
    index1 = index1 + 1
for index0 in range(0,len(list_of_numbers)):
    if list_of_numbers[index0] != max and list_of_numbers[index0] != min:
        SumOfElementsExceptOfMinAndMax = SumOfElementsExceptOfMinAndMax + list_of_numbers[index0]
    index0 = index0 + 1
print ("Maximum: " +str(max))
print ("Minimum: " +str(min))
print ("Sum of elements except of maximum and minimum: " + str(SumOfElementsExceptOfMinAndMax))