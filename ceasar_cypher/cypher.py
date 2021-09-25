def getShift(num, letter):
    #Shift Formula = (num - 4) - letterNum + 1 % 26
    
    letterNum = ord(letter) - 96
    return ((num - 4) - letterNum + 1) % 26

def encode(string, shift): 
    output = ""
    for letter in string:
        if letter != " ":
            shiftedLetter = ord(letter)+shift
            if shiftedLetter > 122:
                shiftedLetter = shiftedLetter - 26
            output += chr(shiftedLetter)
        else:
            output += " "
    return output

def decode(string, shift): 
    output = ""
    for letter in string:
        if letter != " ":
            shiftedLetter = ord(letter)-shift
            if shiftedLetter < 97:
                shiftedLetter = shiftedLetter + 26
            output += chr(shiftedLetter)
        else:
            output += " "
    return output


message = ["water is important", "maths is fun", "they are coming", "friends make me happy", "i love school"]
nums = [15, 1, 7, 8, 12]
letters = ['s', "a", "t", "u", "l"]

decoded = []
for i in range(5):
    print(str(nums[i]) + letters[i])
    encrypted = encode(message[i], getShift(nums[i], letters[i]))
    print(encrypted)
    decoded.append(decode(encrypted, getShift(nums[i], letters[i])))


print(decoded)
