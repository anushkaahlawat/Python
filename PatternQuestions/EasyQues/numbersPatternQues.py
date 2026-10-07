'''1.print :
1
12
123
1234  '''


#for i in range(1,5):
 #   for j in range(1, i + 1):
 #     print(j, end ="")
 #   print()


'''2.print :
1
22
333
4444  '''


#for i in range(1,5):
#   for j in range(1,i + 1):
#      print(i,end ="")
#   print()
      

'''3.print :
1234
1234
1234
1234  '''


#for i in range(1,5):
 #   print("1234")

'''4.print :
1
2
3
4
5  '''

#for i in range(1,6):
 #   print(i)

'''5.
5
54
543
5432
54321  '''


#for i in range(1, 6):
#    for j in range(5, 5-i, -1):
#        print(j, end="")
#    print()

'''6.
12345
1234
123
12
1  '''


for i in range(5,0,-1):
    for j in range(1,i + 1):
        print(j,end="")
    print()