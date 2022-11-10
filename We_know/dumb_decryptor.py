our_text = input("Enter text to decrypt: ")
Caesar_key = int(input("Enter value of Caesar key: "))
alphabet_small = "abcdefghijklmnopqrstuvwxyzabcdefghigklmnopqrstuvwxyz"
alphabet_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
result = ""
for letter in our_text:
    basic_place = alphabet_big.find(letter)
    new_place = basic_place + Caesar_key
    
    if letter in alphabet_big:
        result = result + alphabet_big[new_place]
    else:
        result = result + letter
print (result)