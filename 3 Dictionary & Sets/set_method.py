collection=set()
collection.add(1)
collection.add(2)
collection.add((1,2,3))
collection.add("hello world")

collection.remove(1)
print(collection)
print(len(collection))

#union of sets
set1={1,2,3}
set2={3,4,5}
set3=(set1.union(set2))
print(set3)
set4=(set1.intersection(set2))
print(set4)