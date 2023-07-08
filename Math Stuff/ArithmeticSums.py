""" import time
import sys
# add two variables named Upper_Limit and Lower_limit

Upper_Limit = int(input("Upper limit:"))
Lower_Limit = int(input("Lower limit x = "))
time.sleep(.3)
limits = [Lower_Limit, Upper_Limit]
time.sleep(.3)
print("default limits are", Upper_Limit, "and", Lower_Limit)
time.sleep(.5)


if Upper_Limit > Lower_Limit:
    print("Proceed")
else:
    print("Upper Limit cannot be larger than lower limit")
    time.sleep(1)
    sys.exit()

time.sleep(.5)
equation = input("Equation: ")

# Unfinished, keep adding equation and figure out how to get the input of the equation to work
"""
# Its a lot easier than I thought
# Whole numbers only
var n = 100 // upper bound
var a = 1 // lower bound
var sum = (n * (n + a)) / 2 // sum of all numbers from 1 to n