list = str(input("Enter numbers: "))
list1 = list.split(", ")
index1 = 1
index0 = 0
max= int(list1[0])
min= int(list1[0])
SumOfElementsExceptOfMinAndMax = 0 
#while index1 < int(list1[-1]):
#for index1 in list1:
if int(list1[index1]) > max:
    max = list1[index1]
elif int(list1[index1]) < min:
    min = list1[index1]
index1= index1+1
if int(list1[index0]) != max and int(list1[index0]) != min:
    SumOfElementsExceptOfMinAndMax = SumOfElementsExceptOfMinAndMax + int(list1[index0])
index0 = index0+1
print ("max: " +str(max))
print ("min: " +str(min))
print ("Sum of elements except of maximum and minimum: " + str(SumOfElementsExceptOfMinAndMax))
print (list1)
