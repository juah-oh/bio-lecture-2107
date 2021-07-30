#!/bin/bash

for i in `cat list.txt`
do
    echo "${i}"
done

for i in $(cat list.txt)
do
    echo "${i}"
done

