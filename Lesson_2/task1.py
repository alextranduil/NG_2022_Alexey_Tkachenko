string = input("Enter string of liters: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = {}
for element in alphabet:
  amount = string.count(element)
  if amount > 0:
    print (str(element) +" - "+ str(amount)) # 2- Вывести количество каждой буквы отдельно
    result[element]=int(amount)
    sorted_result = dict(sorted(result.values(), reverse=True))
print (result)
print(sorted_result)