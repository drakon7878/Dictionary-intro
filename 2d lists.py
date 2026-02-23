list1 = [[1,2,3], [4,5,6], [7,8,9]]

#print(list1)
#print(len(list1))

#print(list1[0])

#print(list1[2][1])
#print(list1[1][1])

#for i in range(0,len(list1)):
 #   for j in range(0,len(list1[0])):
  #      print(list1[i][j] , end = " ")
   # 
    #print("\n")

rows = int(input("Type the number of rows here -->"))
columns = int(input("Type the number of columns here-->"))

matrix = []
#input loop
for i in range(rows):
    temp  = []
    for j in range(columns):
        a = int(input("Enter your element -->"))
        temp.append(a)

    matrix.append(temp)

#output loop
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end = " ")
    
    print("\n")

    

