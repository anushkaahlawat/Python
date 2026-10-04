'''1. Star Triangle
*
**
***
****
***** '''


#for i in range(1,6):
 #   print("*"*i)



'''2. Inverted Star Triangle
*****
****
***
**
* '''


#for i in range(5,0,-1):
 #   print("*"*i)



'''3. Number Triangle
1
12
123
1234
12345 '''


#for i in range(1,6):
#    for j in range(1,i + 1):  
#     print(j,end = "")
#    print()



'''4. Repeated Number Triangle
1
22
333
4444
55555 '''



#for i in range(1,6):
#    for j in range(1,i + 1):
 #       print(i,end = "")
 #   print()



'''5. Reverse Number Triangle
54321
5432
543
54
5 '''


#for i in range(5,0,-1):
#    for j in range(5,5-i,-1):
#        print(j,end = "")
 #   print()



'''6. Increasing Number Rows
1
23
456
78910 '''


#num = 1

#for i in range(1,5):
#    for j in range(1,i + 1):
#        print(num,end = "")
#        num += 1
#    print()


'''7. Same Number in Every Row
11111
22222
33333
44444
55555 '''



#for i in range(1,6):
#    for j in range(5):
#        print(i,end = "")
#    print()



'''8. Alphabet Triangle
A
AB
ABC
ABCD
ABCDE '''


#for i in range(1,6):
#    for j in range(1,i + 1):
#        print(chr(64 + j),end = "")
#    print()


'''9. Repeated Alphabet
A
BB
CCC
DDDD
EEEEE '''


#for i in range(1,6):
#    for j in range(1,i + 1):
#        print(chr(64 + i),end = "")
#    print()

'''10. Reverse Number Triangle
12345
1234
123
12
1 '''


#for i in range(5,0,-1):
#    for j in range(1,i + 1):
#        print(j, end = "")
#    print()

'''11. Odd Numbers
1
13
135
1357
13579 '''



#for i in range(1,6):
#    for j in range(1,1 + i):
#        print(2 * j - 1,end = "")
#    print()



'''12. Even Numbers
2
24
246
2468
246810 '''


#for i in range(1,6):
#    for j in range(1,1 + i):
#        print(2 * j,end = "")
#    print()



'''13. Counting Pattern
1
22
333
4444
55555 '''


#for i in range(1,6):
#    for j in range(1,1 + i):
#        print(i, end = "")
#    print()



'''14. Reverse Counting
5
44
333
2222
11111 '''



#for i in range(1,6):
#    for j in range(i):
#        print(6 - i, end = "")
#    print()



'''15. Alternating Pattern
0
11
000
1111
00000 '''



#for i in range(1, 6):
#    for j in range(1, i + 1):
#     if i % 2 == 0:
 #           print(1, end="")
 #       else:
 #           print(0, end="")

 #   print()



'''15. Alternative pattern
1
01
101
0101
10101 '''



for i in range(1, 6):
    for j in range(1, i + 1):
        if (i + j) % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
    print()



