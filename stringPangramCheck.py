inputStr = input("Input your string here-->")

alphabet = {
    'a' : 0,
    'b':0,
    'c':0,
    'd':0,
    'e':0,
    'f':0,
    'g':0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0,
}

def main():
    for letter in inputStr:
        if letter in alphabet:
            alphabet[letter] +=1
    
    pangram = True
    for count in alphabet.values():
        if count == 0:
            pangram = False

    if pangram:
        print("This string is a Pangram")
    else:
        print("This string is not a pangram")

while type(inputStr) != str:
    print("The input you have given is not a string. Pleaee input a string")
    inputStr = input("Input your string here-->")

main()
