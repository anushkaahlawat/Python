'''1. Right-aligned star triangle
    *
   **
  ***
 ****
***** '''



#for i in range(1,6):
#    print(" " *(5-i) + "*" * i)



'''2. Inverted number triangle
12345
1234
123
12
1 '''



#for i in range(5,0,-1):
#    for j in range(1,i + 1):
#        print(j ,end = "")
#    print()



'''3. Repeated row-number triangle
1
23
345
4567
56789 '''


'''num = 1

for i in range(1,6):
    for j in range(1, i + 1):
        print(num , end = "")
        num = num + 1
    print()'''



'''4. Floyd's triangle
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15 '''



#num = 1

#for i in range(1,6):
#    for j in range(1,i + 1):
#        print(num , end = " ")
#        num = num + 1
#    print()



'''5. Binary triangle
1
01
101
0101
10101 '''



#for i in range(1,6):
#    for j in range(1, i + 1):
#        if (i + j) % 2 == 0:
#            print("1",end = "")
#        else:
#            print("0", end = "")
#    print()


'''6. Palindrome number pyramid
    1
   121
  12321
 1234321
123454321 '''


'''7. Number pyramid
    1
   123
  12345
 1234567
123456789 '''


'''8. Continuous reverse number triangle
12345
6789
101112
1314
15 '''


'''9. Pascal's triangle
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1 '''


'''10. Increasing alphabet triangle
A
AB
ABC
ABCD
ABCDE '''



#for i in range(1,6):
#    for j in range(1, i+1):
#        print(chr(64 + j), end = "")
#    print()



'''11. Repeated alphabet triangle
A
BB
CCC
DDDD
EEEEE '''



#for i in range(1,6):
#    for j in range(1, i + 1):
#        print(chr(64 + i), end = "")
#    print()



'''12. Continuous alphabet triangle
A
BC
DEF
GHIJ
KLMNO '''



#char = 65


#for i in range(1,6):
#    for j in range(1, i + 1):
#        print(chr(char), end = "")
#        char = char + 1
#    print()



'''13. Inverted alphabet triangle
ABCDE
ABCD
ABC
AB
A '''


#for i in range(5,0,-1):
#    for j in range(1, i + 1):
#        print(chr(64 + j), end = "")
#    print()



'''14. Alphabet palindrome pyramid
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA '''


'''15. Hollow right triangle
*
**
* *
*  *
***** '''



#for i in range(1,6):
#    if i == 1:
#        print("*")
#    elif i == 2:
#        print("**")
#    elif i == 3:
#        print("* *")
#    elif i == 4:
#        print("*  *")
#    else:
#        print("*****")




'''16. Hollow pyramid
    *
   * *
  *   *
 *     *
********* '''


'''17. Hollow inverted pyramid
*********
 *     *
  *   *
   * *
    * '''


'''18. Hollow diamond
    *
   * *
  *   *
 *     *
  *   *
   * *
    * '''



#for i in range(1,8):
#    if i == 1 or i == 7:
#        print("   *")
#    elif i == 2 or i == 6:
#        print("  * *")
#    elif i == 3 or i == 5:
#        print(" *   *")
#    else:
#        print("*     *") 


'''19. Diamond star pattern
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    * '''


'''20. Inverted number pyramid
123456789
 1234567
  12345
   123
    1 '''


'''21. Alternating star triangle
*
**
***
****
*****
****
***
**
* '''


'''22. Number diamond
    1
   121
  12321
 1234321
123454321
 1234321
  12321
   121
    1 '''


'''23. Concentric number square

For n = 4, the pattern is:

4444444
4333334
4322234
4321234
4322234
4333334
4444444 '''


'''24. Multiplication triangle
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25 '''


'''25. X pattern
*   *
 * *
  *
 * *
*   * '''



#for i in range(1,6):
#    if i == 1 or i == 5:
#        print("*   *")
#    elif i == 2 or i == 4:
#        print(" * *")
#    else:
#        print("  *")



'''26. Plus pattern
  *
  *
*****
  *
  * '''



#for i in range(1,6):
#    if i == 1 or i == 5:
#        print("  *")
#    elif i == 2 or i == 4:
#        print("  *")
#    else:
#        print("*****")



'''27. Hourglass pattern
*****
 ****
  ***
   **
    *
   **
  ***
 ****
***** '''


'''29. Hollow square
*****
*   *
*   *
*   *
***** '''


'''30. Hollow right triangle
*
**
* *
*  *
***** '''


