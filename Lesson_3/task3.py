def countEachElementInString(index):
    element = string[index]
    result[element] = string.count(element)
    indexing(index)

def indexing(index):
    if index < len(string)-1:
        index = index + 1
        countEachElementInString(index)
    else:
        print(result)

index = 0
result = {}
string = input("Enter string: ")
countEachElementInString(index)