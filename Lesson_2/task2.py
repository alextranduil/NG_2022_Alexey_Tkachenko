list = str(input("Enter list separated by commas: "))
print (list.split(","))
list1 = list.split(",")
i = 1
#while i < len(list1):
for element in list1:
    if element[i] == element[0]:
        list1.pop(i)
        i = i+1
print (list1)