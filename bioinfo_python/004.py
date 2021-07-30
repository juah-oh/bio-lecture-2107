#!/usr/bin/python3

import sys
#num1 = 3
num1 = int(sys.argv[1])

if num1 % 2 == 0:
    print("짝수")
elif num1 % 2 == 1:
    print("홀수")


