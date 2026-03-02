length = int(input("Input the dimensions of your matrix here -->"))
matrix = []

for i in range(length):
    temp = []
    for j in range(length):
        temp.append(int(input("Type your element here-->")))
    
    matrix.append(temp)

temp2 = []
trace = 0
for i in range(length):
    trace += matrix[i][i]
    temp2.append(matrix[i][i])


print(trace)