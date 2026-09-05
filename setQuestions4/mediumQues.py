# 1.Find the union of two sets.


'''s1 = {1,2,3,4}
s2 = {5,6,7,4,3}

print(s1.union(s2))'''



#---------------------------------------------------------------------------------------------------------



# 2.Find the intersection of two sets.


'''set1 = {1,2,3,4,5}
set2 = {2,3,4,5,7,8}

print(set1.intersection(set2))'''



#----------------------------------------------------------------------------------------------------------



# 3.Find the difference between two sets.


"""se1 = {1,2,3,4,5}
se2 = {6,7,8,9,3}


result = se1 - se2
print(result)"""



#-----------------------------------------------------------------------------------------------------------



# 4.Find the symmetric difference of two sets.



'''s3 = {1,2,3,4}
s4 = {5,7,6,8}

res = s3 ^ s4
print(res)'''



#-----------------------------------------------------------------------------------------------------------



# 5.Remove duplicate elements from a list using a set.


"""num = [1,2,3,4,5,6,7,2,1,4,5,3]

uniq_num = set(num)
print(uniq_num)"""



#------------------------------------------------------------------------------------------------------



# 6.Check whether one set is a subset of another.



'''s1 = {1, 2}
s2 = {1, 2, 3, 4}


if s1.issubset(s2):
    print("s1 is a subset of s2")
else:
    print("s1 is not a subset of s2")'''



#-------------------------------------------------------------------------------------------------------



# 7.Check whether two sets are disjoint.



"""set3 = {1,2,3}
set4 = {3,4,5,6}

if set3.isdisjoint(set4):
    print("sets are disjoined")
else:
    print("sets are not disjoined")"""



#-------------------------------------------------------------------------------------------------------


# 8.Find the common elements in two sets.



"""s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

for i in s1:
    if i in s2:
        print(i)"""



#--------------------------------------------------------------------------------------------------------



# 9.Count the number of elements in a set.


"""set = {1,2,3,4,5,6,7,8,9,10}
count = 0


for i in set:
    count += 1
    print("the numbers of elements is :",count)"""



#--------------------------------------------------------------------------------------------------------



# 10.Find all unique elements from two lists using sets.



list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

s1 = set(list1)
s2 = set(list2)

unique = s1 | s2

print(unique)
