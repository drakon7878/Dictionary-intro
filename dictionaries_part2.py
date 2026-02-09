
#Vowels

inputString = input("Type your string here--> ")
vowels = {
    'a' : 0,
    'e' : 0,
    'i' : 0,
    'o' : 0,
    'u' : 0,
}

for c in inputString:
    if c in vowels:
        vowels[c] +=1


print(vowels)



#Each alphabet
inputString2 = input("Type your string here-->")
charCount = {}
for c in inputString2:
    if c.isalpha():
        if c in charCount:
            charCount[c] +=1
        else:
            charCount[c] = 1

print(charCount)


#Numbers

inputInt = input("Type your number here-->")

numbers={
    '1' : 0,
    '2' : 0,
    '3' : 0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0,
    '0':0,
}

for num in inputInt:
    if num in numbers:
        numbers[num] +=1

pangram = True
for count in numbers.values():
    if count == 0:
        pangram = False

if pangram:
    print("This number is a pangram")
else:
    print("The number is not a pangram")