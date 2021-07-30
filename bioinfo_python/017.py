#!/usr/bin/python3

fw = open("writ_sample.txt" , "w")
fw.write("MEN1|n")
fw.close()

#권장하는 방식은 아니지만 띄어쓰기가 너무 중복될때 쓸 수 있는 방식이다

with open("writ_sample2.txt" , "w") as write_handle:
    write_handle.write("BRCA1|n")

with open("writ_sample2.txt" , "a") as write_handle:
    write_handle.write("BRCA2|n")
#추가하기
