#!/usr/bin/python3

#Check the data found by the player and return the flag if success
#    no input.
#    require : flag in ./flag.txt


rproto="6"
ans = input("What is the real protocol over IP number ?  ")
proto = str(ans)

if proto != rproto:
    print("Sorry, keep trying")
    exit(1)

else:
    fd=open("flag.txt")
    flag=fd.read()
    print("Congratulation ! The flag is : "+flag+" \n")
    exit(0)
