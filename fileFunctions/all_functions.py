file = open("test.txt", "w")
file.write("Hello world\n")
file.write("1234\n")

file.close()

file = open("test.txt", "a")
file.write("2nd Hello\n")
file.write("5678\n")

file.close()

file= open("test.txt", "r")
data = file.read()
print(data)

file.seek(1)
print(file.readline())

file.close()



file = open("test.txt", "a+")
file.write("Hi I'm Jaivin")
print(file.read())
file.close()

file.seek()
