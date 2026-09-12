# print numberss from 1 to 100 using while loop



"""i = 1
while i <= 100:
    print(i)
    i += 1"""


# print numbers from 100 to one using while loop



"""i = 100
while i >= 1:
    print(i)
    i -= 1"""


# print multiplication table of a number n.



"""n = int(input("enter a number :"))
i = 1                                                    # n is the number 
while i <= 10:
    print(n*i)
    i += 1"""


# print the elements of the following list using loops-[1,4,9,16,25,36,49,64,81,100]



"""number = [1,4,9,16,25,36,49,64,81,100]

index = 0
while index < len(number):
    print(number[index])
    index += 1"""



# search for a number X in this tuple using loops: (1,4,9,16,25,36,49,64,81,100)



tup = (1,4,9,16,25,36,49,64,81,100)

x = 36
i= 0
while i < len(tup):
    if (tup[i] == x):
        print("number is found :",i)
    i += 1


