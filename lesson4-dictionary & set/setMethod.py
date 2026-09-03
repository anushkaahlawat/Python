# 1. set.add(el) method                                   # adds an element



'''collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add(5)
collection.add(1)

print(collection)'''



# 2. set.remove(el) method                                # remove an element



'''diary = set()

diary.add("pencil")
diary.add("rubber")
diary.add("sketch")
diary.add("more")

diary.remove("more")

print(diary)'''



# 3. set.clear() method                                    # empties the set


call = set()

call.add("hello")
call.add("hiii")
call.add("weee")
call.add("woohhh")

call.clear()

print(len(call))



# 4. set.pop() method                                      # removes an random value


cube = {"python","java","c","c++","html","javaScript","css"}

print(cube.pop())
print(cube.pop())
print(cube.pop())
print(cube.pop())



# 5. set.union(set2)                                        # combine both set values and returns new



s1 = {1,2,3,4}
s2 = {3,4,5,6}


print(s1.union(s2))



# 6. set.intersection(set2)                                 # combine common values and returns new



set1 = {1,2,3,4}
set2 = {3,4,5,6}


print(set1.intersection(set2))


