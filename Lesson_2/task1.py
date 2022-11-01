string = input("Enter string of liters: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = {}
for element in alphabet:
  amount = string.count(element) # 1 - Count the number of each letter in a string.
  if amount > 0:
    print (str(element) +" - "+ str(amount)) # 2 - Print the number of each letter separately
    result[element]=int(amount) 
print (result)
sorted_values = sorted(result.values(), reverse=True) # 3 - Sort the number by the letters themselves
sorted_result = {}
for value in sorted_values:
    for index in result.keys():
        if result[index] == value:
            sorted_result[index] = result[index]
print(sorted_result)