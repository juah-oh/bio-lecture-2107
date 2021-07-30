#!/usr/vin/python3

import sys

try:
    with open("noname.txt" , "r") as handle:
        read = handle.readlines()

except FileNotFoundError:
    print("파일이 없습니다")
    sys.exit()

print(read)

