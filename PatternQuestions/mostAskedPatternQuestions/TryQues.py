####   Level --- 1   Must Try pattern Questions 


'''1. ⭐ Increasing number triangle
1
12
123
1234
12345 '''



#for i in range(1,6):
#    for j in range(1, 1 + i):
#        print(j,end = "")

#    print()



'''2. ⭐ Inverted number triangle
12345
1234
123
12
1 '''



#for i in range(5,0,-1):
#    for j in range(1, 1 + i):
#        print(j ,end = "")

#    print()



'''3. ⭐ Repeated number triangle
1
22
333
4444
55555 '''



#for i in range(1,6):
#    for j in range(1, 1 + i):
#        print(i, end = "")

#    print()



'''4. ⭐ Right-aligned number triangle
    1
   12
  123
 1234
12345 '''



#for i in range(1,6):
#    print(" " * (5 - i),end = "")

#    for j in range(1, 1 + i):
#        print(j ,end = "")

#    print()



'''5. ⭐ Inverted number triangle with spaces
12345
 1234
  123
   12
    1 '''



#for i in range(5,0,-1):
#    print(" " * (5 - i),end = "")

#    for j in range(1, 1 + i):
#        print(j ,end = "")

#    print()




'''6. ⭐ Continuous alphabet triangle
A
BC
DEF
GHIJ
KLMNO '''



#num = 65

#for i in range(1,6):
#    for j in range(1, 1 + i):
#        print(chr(num),end = "")
#        num = num + 1

#    print()



###  Level -- 2  Important pyramid pattern questions


'''7. Number pyramid
    1
   123
  12345
 1234567
123456789 '''



#for i in range(1,6):
#    print(" " * (5 - i),end = "")

#    for j in range(1,2*i):
#        print(j,end = "")

#    print()



'''8. ⭐ Inverted number pyramid
123456789
 1234567
  12345
   123
    1 '''



#for i in range(5,0,-1):
#    print(" " * (5 - i),end = "")

#    for j in range(1,2*i):
#        print(j,end = "")

#    print()



'''9. ⭐ Palindrome number pyramid
    1
   121
  12321
 1234321
123454321 '''



#for i in range(1,6):
#    print(" " * (5 - i),end = "")

#    for j in range(1,1 + i):
#        print(j,end = "")

#    for j in range(i-1,0,-1):
#        print(j,end = "")

#    print()


'''10. ⭐ Diamond star pattern
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    * '''



for i in range(1,6):
    print(" " * (5 - i) + "*" * (2*i-1))

for i in range(5,0,-1):
    print(" " * (5 - i) + "*" * (2*i-1))





