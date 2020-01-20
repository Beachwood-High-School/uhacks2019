#!/bin/bash
#i goes from 0 to target
num = 10
echo ""|tee out
for i in {0..$(($num-1))}
do
         python intlinks.py $(($i*10+1))| tee -a out &
         python intlinks.py $(($i*10+2))| tee -a out &
         python intlinks.py $(($i*10+3))| tee -a out &
         python intlinks.py $(($i*10+4))| tee -a out &
         python intlinks.py $(($i*10+5))| tee -a out &
         python intlinks.py $(($i*10+6))| tee -a out &
         python intlinks.py $(($i*10+7))| tee -a out &
         python intlinks.py $(($i*10+8))| tee -a out &
         python intlinks.py $(($i*10+9))| tee -a out &
         python intlinks.py $(($i*10+10))| tee -a out
         echo "ALL "$(($i+1))
done  
