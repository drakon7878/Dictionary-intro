marksMaths = []
marksEnglish = []
marksScience = []
name = input("Type the student's name here-->")

result = (name, marksMaths, marksEnglish, marksScience)
subjects = {
                            1 : "Maths",
                            2: "English",
                            3: "Science"
                        }
for i in range(3):
    print("Cycle "+str(i+1)+" of Tests\n")
    for j in range(3):
        markEnter = int(input("Enter the marks for "+subjects[j+1]+" -->"))
        globals()[f"marks"+subjects[j+1]].append(markEnter)


MathsAverage = 0
EnglishAverage= 0
ScienceAverage = 0

for i in range(1,4,1):
    for j in range(3):
        globals()[f""+subjects[i]+"Average"] += result[i][j]

    globals()[f""+subjects[i]+"Average"] = (globals()[f""+subjects[i]+"Average"] / 240)*100
                  

print("Student Name:", result[0],"\n")
if MathsAverage > 50 and EnglishAverage > 50 and ScienceAverage > 50:
    print(result[0],"has passed!!")
else:
    print(result[0], "has failed😢")
