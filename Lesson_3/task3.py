def countEachElementInString(index, result, string):
    if index < len(string):
        element = string[index]
        result[element] = string.count(element)
        return countEachElementInString(index + 1, result, string)
    return result

index = 0
result = {}
string = input("Enter string: ")
print(countEachElementInString(index, result, string))