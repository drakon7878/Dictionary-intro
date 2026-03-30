from random import randint
secretList = []

for i in range(3):
    temp = randint(0,5)
    secretList.append(temp)
    print(i)

secret = set(secretList)
extra = secret



print("Below, you will get to input 3 numbers one at a time.\nYour goal is to the guess the 3 numbers in a secret set.\nThe numbers can be from 0-5")
print("Your guesses may not be in the same order as the set.")
wrong = False
limit = 0
userSet = set([])
while limit < 3:
    guess = int(input("Type your number here-->"))
    userSet.add(guess)
    limit+=1

check = secret & userSet

if check == secret:
    print("You have correctly guessed the secret set which was", extra)
else:
    print("The set was", extra)
