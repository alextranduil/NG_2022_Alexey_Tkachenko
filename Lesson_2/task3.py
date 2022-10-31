size = int(input("Input size: "))
safed_size= size
pattern = [str(size)]
while size > 1:
    size = size - 1
    pattern.append(str(size))
print (" ".join(pattern))
while safed_size > 1:
    pattern.pop(0) 
    print (" ".join(pattern))
    safed_size = safed_size -1 