#!/usr/bin/python3

#Check the data found by the player and return the flag if success
#    no input.
#    require : flag in ./flag.txt


rans='726'

inp = input("Find the size of the legitimate http answer (in Bytes) :  ")
ans = str(inp)

if rans != ans:
    print("Try again, hold on !")
    exit(1)

else:
    fd=open("flag.txt")
    flag=fd.read()
    print("Congratulation ! The flag is : "+flag+" \n")
    exit(0)
