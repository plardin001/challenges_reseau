#!/usr/bin/python3

#Check the data found by the player and return the flag if success
#    input : user answer (string)
#    require : answer in ./.answer.txt
#    require : flag in ./flag.txt

import sys

if len(sys.argv) == 1:
    print("Please give your answer in argument")
    exit(1)
if len(sys.argv) != 2:
    print("Please give your answer in argument in a string format")

uans=sys.argv[1]
fd=open('.answer.txt')
ans=fd.read()
if uans == ans:
    fd=open("flag.txt")
    flag=fd.read()
    print("Congratulation ! The flag is : "+flag+" \n")
else:
    print("Sorry, wrong answer.. keep trying  !")