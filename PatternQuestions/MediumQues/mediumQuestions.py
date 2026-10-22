''' 16. Alphabet triangle
A
BC
DEF
GHIJ
KLMNO '''


#num = 65

#for i in range(1,6):
#    for j in range(1, i + 1):
#        print(chr(num),end = "")
#        num = num + 1

#    print()


'''17. Repeated alphabet triangle
A
BB
CCC
DDDD
EEEEE '''



#for i in range(1,6):
#    for j in range(1 , i + 1):
#        print(chr(64 + i),end = "")

#   print()



'''18. Reverse alphabet triangle
ABCDE
ABCD
ABC
AB
A '''



#for i in range(5,0,-1):
#    for j in range(1,i + 1):
#        print(chr(64 + j),end = "")

#    print()
    


'''19. X pattern
*   *
 * *
  *
 * *
*   * '''



for i in range(1,6):
    if i == 1 or i == 5:
        print("*   *")
    elif i == 2 or i == 4:
        print(" * *")
    else:
        print("  *")




'''20. Plus pattern
  *
  *
*****
  *
  *  '''



#for i in range(1,6):
#    if i == 3 :
#        print("*****")
#    else:
#        print("  *")


