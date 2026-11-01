###  Level -- 3  Hollow Pattern Questions


'''11. Hollow rectangle
******
*    *
*    *
****** '''



#for i in range (1,5):
#   if i == 1 or i == 4:
#       print("******")
#   else:
#        print("*    *")




'''12. ⭐ Hollow pyramid
    *
   * *
  *   *
 *     *
********* '''



#for i in range (1,6):
#    if i == 1:
#       print(" " * (5 - i) + "*")
#    elif i == 5:
#       print("*" * 9)
#    else:
#       print(" " * (5 - i) + "*" + " " * (2 * i - 3) + "*")




'''13. Hollow inverted pyramid
*********
 *     *
  *   *
   * * 
    * '''



#for i in range(1, 6):
#    if i == 1:
#        print("*" * 10)
#    elif i == 5:
#        print(" " * 4 + "*")
#    else:
#        print(" " * (i - 1) + "*" + " " * (12 - 2 * i) + "*")




'''14. ⭐ Hollow diamond
    *
   * *
  *   *
 *     *
  *   *
   * *
    * '''




#for i in range(1, 8):
#    if i == 1 or i == 7:
#        print("   *")
#    elif i == 2 or i == 6:
#        print("  * *")
#    elif i == 3 or i == 5:
#        print(" *   *")
#    else:
#        print("*     *")




### Level -- 4  Number and alphabet challenges



'''15. Floyd's triangle ⭐
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15 '''



'''16. Binary triangle
1
01
101
0101
10101 '''



'''17. Reverse alphabet triangle
ABCDE
ABCD
ABC
AB
A '''



#for i in range(5,0,-1):
#    for j in range (1, i + 1):
#        print(chr(64 + j) , end = "")
#    print()




'''18. Repeated alphabet triangle ⭐
A
BB
CCC
DDDD
EEEEE '''



#for i in range(1,6):
#    for j in range(1 , i + 1):
#        print(chr(64 + i),end = "")
#    print()




'''19. Continuous alphabet triangle in reverse
ABCDE
FGHI
JKL
MN
O '''



#num = 65

#for i in range(5,0,-1):
#    for j in range(1, i + 1):
#        print(chr(num),end = "")
#        num = num + 1
#    print()




'''20. Number staircase ⭐
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5 '''



#for i in range (1,6):
#    for j in range(1,i + 1):
#        print(i, end = " ")
#    print()

