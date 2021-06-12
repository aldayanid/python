#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#F to C conversion
#print("Enter the temperature in Farenheit:")
#out_cel=(in_far-32)/1.8
#out_far=(in_cel+32)*1.8

corf=input ("Celsius or Farenheit:")
if corf == "F" or corf == "f":
        print("Enter the temperature in Farenheit:")
        in_far=float(input())
        out_cel=(int(in_far)-32)/1.8
        print("In Celsius is: " + str(round(out_cel, 2))+"°C.")
elif corf == "C":
        print("Enter the temperature in Celsius:")
        in_cel=float(input())
        out_far=(int(in_cel)+32)*1.8
        print("In Fahrenheit is: " + str(round(out_far, 2))+"°F.")
else:
        print("Error")


# print("For Celsius to Fahrenheit type C/c \n or F/f for Fahrenheit to Celsius"
# if input() == C or input() == c:
#     FtoC = input ("Enter the temperature in Farenheit:")
#     out_C=(int(FtoC)-32)/1.8
#     print(f"Result in Celsius is: ${out_C}°C.")
# else:
#     CtoF = input ("Enter the temperature in Celsius:")
#     out_F=(int(CtoF)+32)*1.8
#     print(f"Result in Celsius is: ${out_F}°C.")