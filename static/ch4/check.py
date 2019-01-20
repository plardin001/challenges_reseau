#!/usr/bin/python3

#Check the data found by the player and return the flag if success
#    no input.
#    require : flag in ./flag.txt


ruser="fake"
rmdp="1user"

ans1 = input("Please enter the user name : ")
user= str(ans1)

if ruser != user:
    print("Sorry, keep trying")
    exit(1)

else:
    print("Well done !")
    print("Please now enter the password : ")
    ans2 = input("Please enter the user name : ")
    mdp= str(ans2)

    if rmdp != mdp:
        print("Sorry, keep trying")
        exit(1)

    else:
        fd=open("flag.txt")
        flag=fd.read()
        print("Congratulation ! The flag is : "+flag+" \n")
        exit(0)
