#!/usr/bin/bash

import sys

def make_douvle(num):
    return num * 2

if len(sys.argv) !+ 2:
    print(f"#usage: python {sys.argv[0]} [number]")
    sys.exit()

num = int(sys.argv[1])
result = make_double(num)
print(result)



