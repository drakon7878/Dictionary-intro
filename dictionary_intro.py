sample_dict = {
    "name" : "Jaivin",
    "age" : 14,
    "class": "8th",
}

print(sample_dict["name"])
print(sample_dict)

sample_list = ["Jaivin", 14 , '8th']

print(sample_list[0])
print(sample_dict.keys())
print(sample_dict.values())

for key in sample_dict.keys():
    print(key , sample_dict[key])

if "gender" in sample_dict:
    print(sample_dict["gender"])
else:
    print("key does not exist")

sample_dict["school"] = "Spring Dale Senior School"

print(sample_dict)

del(sample_dict["class"])
print(sample_dict)

sample_dict["name"] = "Jaivin Singh Saini"
print(sample_dict)

sample_dict["marks"] = [95,96,97,98,99]
print(sample_dict)

print(sample_dict["marks"][1])


classroom = {
    "Jaivin" : {
        "age" : 14,
        "class": "8th",
        "marks": [95,96,97,98,99],
    },
    "Samar" : {
        "age" : 14,
        "class": "8th",
        "marks": [99,98,97,96,95],
    }
}

print(classroom)
print(classroom.keys())
print(classroom.values())

for i in classroom.keys():
    print(classroom[i])

classroom["Samar"]["age"] = 17
print(classroom)