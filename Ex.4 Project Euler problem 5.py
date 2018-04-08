# Kirsty O;Brien 18/03/2018
# Project Euler solution to Q5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20


candidate = 1
result = 0

while result < 1:
    if candidate % 2 == 0 and candidate % 3 == 0 and candidate % 4 == 0 and candidate % 5 == 0 and candidate % 6 == 0 and candidate % 7 == 0 and candidate % 8 == 0 and candidate % 9 == 0 and candidate % 10 == 0 and candidate % 11 == 0 and candidate % 12 == 0 and candidate % 13 == 0 and candidate % 14 == 0 and candidate % 15 == 0 and candidate % 16 == 0 and candidate % 17 == 0 and candidate % 18 == 0 and candidate % 19 == 0 and candidate % 20 == 0:
       result = result + 1
       print(candidate)       
    else: candidate = candidate + 1
