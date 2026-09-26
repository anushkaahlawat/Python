# WAF to print the length of a list(list is the parameter)


'''
fruits = ["apple","banana","oranges","kiwi","papaya","mango","watermellon"]
colors = ["white","blue","red","black","yellow","pink","green"]

def len_list(list):
    print(len(list))


len_list(fruits)
len_list(colors)'''



# WAF to print the elements of a single list.(list is the parameter)



'''l1 = ["Hello Anushka"]

def print_elem(list):
    for item in list:
        print(item, end = " ")

print_elem(l1)'''



# WAF to find the factorial of n.(n is the parameter)




'''def calc_fact(n):
    fact = 1
    for i in range (1,n+1):
       fact *= i
    print(fact)
   
calc_fact(5)'''




# WAF to convert USD to IND



def converter(usd_val):
    inr_val = usd_val * 95
    print(usd_val, "USD =", inr_val, "INR")


converter(1)






