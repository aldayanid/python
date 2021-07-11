#inputString=input("Enter an elements list, space separated: ")
#list=inputString.split()
from functools import reduce
from math import prod
import operator

list = [1,2,3,4,5,6,7,8,9]
print(list)
print(" ")
#Summing
sum = 0
for num in list:
    sum += int(num)
print("The total sum: ",sum)
#The max valueu
print("The maximum value is: ",max(list))
#Even numbers only
for even in list:
    if even % 2 == 0:
        print("The even numbers: ",even, end = " ")
print("")
#The odd numbers only
for odd in list:
    if odd % 2 > 0:
        print("The odd numbers: ",odd, end = " ")
print("")
#Product
product_list=0
for product_of_list in list:
    product_of_list = prod(list)
print("The list's product is: ",product_of_list, end = " ")
print("")
#Mean
mean_of_list=sum / len(list)
print("The list's mean is: ",mean_of_list, end = " ")
print("")