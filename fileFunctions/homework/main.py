location = "python Game development/homework/fileOperationsHomework/file.txt"

file = open(location , "a+")
file.write("Using append + read mode\n")

file.seek(0)
data = file.read(5) #Reading just the word "Using"
print(data)
file.close

file = open(location , "w")
file.write("Using overwrite")
file.close

