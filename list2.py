n = int(input("Enter the dimensions of the matrix -->"))
matrix = []
for i in range(n):
    temp = []
    for j in range(n):
        x = int(input("Enter your element-->"))
        temp.append(x)
    matrix.append(temp)

for i in range(n):
    print(matrix[i][i])