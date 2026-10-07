'''1. Right-aligned star triangle
    *
   **
  ***
 ****
***** '''



#for i in range(1,6):
#    print(" " * (5-i) + "*" * i)



'''2. Inverted right-aligned triangle
*****
 ****
  ***
   **
    * '''



#for i in range(5,0,-1):
#    print(" " * (5-i) + "*" * i)



'''3. Pyramid
    *
   ***
  *****
 *******
********* '''



#for i in range(1,6):
#    print(" " * (5-i) + "*" * (2*i-1))



'''4. Inverted pyramid
*********
 *******
  *****
   ***
    * '''



#for i in range(5,0,-1):
#    print(" " * (5-i) + "*" *(2*i-1))



'''5. Number pyramid
    1
   123
  12345
 1234567
123456789 '''



#for i in range(1,6):
#    print(" " * (5-i), end = "")

#    for j in range(1,2*i):
#        print(j,end = "")

#    print()
    


'''6. Number palindrome pyramid
    1
   121
  12321
 1234321
123454321 '''


#for i in range(1,6):
#    print(" " * (5-i), end = "")

#    for j in range(1,i + 1):
#        print(j,end = "")

#    for j in range(i-1,0,-1):
#        print(j, end = "")

#    print()



'''7. Diamond
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    * '''



#for i in range(1,6):
#    print(" " * (5-i) + "*" *(2*i-1))

#for i in range(5,0,-1):
#    print(" " * (5-i) + "*" *(2*i-1))



'''8. Hollow square
*****
*   *
*   *
*   *
***** '''


'''9. Hollow rectangle
******
*    *
*    *
****** '''


'''10. Hollow triangle
*
**
* *
*  *
***** '''


'''11. Number pattern
1
22
333
4444
55555
666666 '''



#for i in range(1,7):
#    for j in range(1,i + 1):
#        print(i,end = "")

#    print()



'''12. Continuous number triangle
1
23
456
78910
1112131415 '''


'''13. Reverse continuous numbers
12345
6789
101112
1314
15 '''


'''14.  0-1 triangle
1
01
101
0101
10101 '''



#for i in range(1,6):
#    for j in range(1,i + 1):
#        if (i + j ) % 2 == 0:
#            print(1, end = "")
#        else:
#            print(0, end = "")

#    print()



'''15.  Alternating stars
*
**
***
****
***
**
* '''



#for i in range(1,5):
#    print("*"*i)



#for i in range(4,0,-1):
#    print("*"*i)

    
