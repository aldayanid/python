#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#F to C conversion
#print("Enter the temperature in Farenheit:")
#out_cel=(in_far-32)/1.8
#out_far=(in_cel+32)*1.8

corf=input ("Celsius or Farenheit:")
    if corf == "F":
        print("Enter the temperature in Farenheit:")
        in_far=input()
        out_cel=(int(in_far)-32)/1.8
        print("In Celsius is: " + str(out_cel)+"°C.")
    elif corf == "C":
        print("Enter the temperature in Celsius:")
        in_cel=input()
        out_far=(int(in_cel)+32)*1.8
        print("In Fahrenheit is: " + str(out_far)+"°F.")
    else:
        print ("Error")