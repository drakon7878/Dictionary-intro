#list --> set
list1 = [1,1,2,2,3,3]
set1 = set(list1)
print(set1)

#to check if sets are indexable
#print(set1[1])

#if element in set or not
if 4 in set1:
    print("Yes")
elif 1 in set1:
    print("1 is in set1 but not 4")
else:
    print("No")

#adding element
set2 = set([])
set2.add(4)
set2.add(5)
set2.add(6)
set2.add(4)
print(set2)

#removing
set2.remove(4)
print(set2)
set2.discard(5)
print(set2)


# set operations
#1. union
#2. intersection
#3. difference
#4. symetric difference

a = {1,2,3,4,5,7}
b = {6,8,9,0,7,1}
print(a.union(b))
print(a | b)

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(a - b)

print(a.symmetric_difference(b))
print(a ^ b)

