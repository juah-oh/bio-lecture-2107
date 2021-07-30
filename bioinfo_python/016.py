#!/usr/bin/python3

f = open("read_sample.txt" , "r")
res = f.readlines()
print(res)
f.close()

print("-----")

with open(read_sample.txt , "r") as f:
    res = f.readlines()
    print(res)

print("-----")

with open(read_sample.txt , "r") as f:
    for line in f:
        print(line.strip())
#메모리 효율적인 방법(선생님이 선호하심)

