# WAP to input the users first name and print its length.


name = input("enter your name : ")

print(len(name))
print(type(name))


# WAP to find the occurrance of '$' in a string.


str = " Hi i'm a $ symbol $100.00"

print(str.count("$"))


# WAP to check the number entered by user is odd and even.

num = int(input("enter your number : "))

rem = num % 2

if (rem == 0):
    print ("even number")
else :
    print ("odd number")


    # WAP to check the greatest of 3 number enterd by user.

    number1 = int(input("enter your first number : "))
    number2 = int(input("enter your first number : "))
    number3 = int(input("enter your first number : "))

    if (number1 >= number2 and number2 >= number3):
        print("first number is greatest")
    elif (number2 >= number3):
        print ("second number is greatest")
    else:
       print("third number is greatest")
