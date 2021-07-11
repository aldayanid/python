print ("The original number is : " + str(test_num))
  
# using format() + list comprehension
# decimal to binary number conversion 
res = [int(i) for i in list('{0:0b}'.format(test_num))]
  
# printing result 
print ("The converted binary list is : " +  str(res))
file = open("bin.bin", "wb")
file.write(b"This binary string will be written to sample.bin")
file.close()