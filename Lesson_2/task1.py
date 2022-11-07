input_string = input("Enter string of liters: ")
result = {}
string = set(input_string)
for element in string:
  result[element] = input_string.count(element) # 1 - Count the number of each letter in a string.
print (result)
for key in result.keys():
    print (str(key) +" - "+ str(result[key])) # 2 - Print the number of each letter separately
sorted_values = sorted(result.values(), reverse=True) # 3 - Sort the number by the letters themselves
sorted_result = {}
for value in sorted_values:
    for index in result.keys():
        if result[index] == value:
            sorted_result[index] = result[index]
print(sorted_result)