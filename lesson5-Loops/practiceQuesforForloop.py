# print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]



'''list = [1,4,9,16,25,36,49,64,81,100]

for i in list:
    print(i)'''



# search for a number X in this tuple using loops: [1,4,9,16,25,36,49,64,81,100]



"""tup = (1,4,9,16,25,36,49,64,81,100)

A = 36
idx = 0
for el in tup:
    if (el == A):
        print("element is found",idx)
        break
    idx += 1"""




# question for Forloop and range functions




# print numbers form 1 to 100.



"""for el in range(1,101):
    print(el)
"""


# print numbers from 100 to 1.



"""for i in range(100,0,-1):
    print(i)"""



# print a multiplication table for a number n.



"""n = int(input("enter a number: "))

for i in range(1,11):
    print(n * i)"""




# WAP to find the sum of first n natural numbers using while loop.



'''x = 5
sum = 0

for i in range(1,x+1):
    sum += i
    print("total sum is: ", sum)'''




# WAP to find the factorial of a number using whileloop.




"""n = 3
fact = 1
i = 1

while i <= n:
        fact = fact * i
        i += 1

print(fact)"""




#------------------------------------------------------- or ----------------------------------------------------------------- 




n = 5
fact = 1

for i in range(1,n+1):
    fact = fact * i
print(fact)

