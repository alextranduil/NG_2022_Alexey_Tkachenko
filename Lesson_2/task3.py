size = int(input("Input size: "))
safed_size = size - 1
while safed_size > 0:
    while size > 0:
        print(size, end = ' ')
        size = size - 1
    size = safed_size
    safed_size = safed_size - 1
    print() 
print(1)