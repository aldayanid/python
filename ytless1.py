#birth_year = input ('Birth year: ')
#age = 2021 - int(birth_year)
#print(age)

#lbs = input ('Input pounds: ')
#kilo = int(lbs)*0.45359237
#print (round(kilo, 2))

#import math
#print(math.floor(2.9))
#math module !!!!!

#x = 4 ** 3
#print(x)

#price =1000000
#good_credit = True

#if good_credit:
#    down_payment = 0.1 * price
#else:
#    down_payment = 0.2 * price
#print(f"Down payment: ${down_payment}")

# yName = input("Please input your name: ")

# if (len(yName)) < 3 or (len(yName)) > 50:
#    print("Bad name")
# else:
#    print("Good name")

yourWeight = float(input("Your weight: "))
LBSorKG = input("LBS or KG, please type L/l for Lbs or K/k for Kg: ")
if LBSorKG == "k" or LBSorKG == "K":
        toLbs = yourWeight * 2.20462
        print("Your weight in pounds is: ", str(round(toLbs, 2)), "lbs")
elif LBSorKG == "l" or LBSorKG == "L":
        toKg = yourWeight * 0.453592
        print("Your weight in kilogramms is: ", str(round(toKg, 2)), "kg")
else:
        print("Error")
