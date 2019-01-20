#!/usr/bin/python3

#Check the data found by the player and return the flag if success
#    no input.
#    require : flag in ./flag.txt


rfragsize="1480"
rheadersize="20"
rlastsize="665"
rlastoffset="1295"

ans = input("Give the maximum payload size of a fragment (Bytes): ")
fragsize = str(ans)

if rfragsize != fragsize:
    print("Sorry, keep trying")
    exit(1)
    
else:
    print("Well done !")
    ans = input("Please now enter the size of the IP header (Bytes): ")
    headersize= str(ans)

    if headersize != rheadersize:
        print("Sorry, keep trying")
        exit(1)

    else:
        print("You are doing well ! ")
        ans=input("What is the size of the last fragment ? (Bytes): ")
        lastsize=str(ans)

        if lastsize != rlastsize:
            print("Sorry, please try again")
            exit(1)

        else:
            print("Amazing ! ")
            ans=input("The last question : What is the last fragment's offset ? ")
            lastoffset=str(ans)
            if lastoffset != rlastoffset:
                print("Sorry, please try again")
                exit(1)                
        
            else:
                fd=open("flag.txt")
                flag=fd.read()
                print("Congratulation ! The flag is : "+flag+" \n")
                exit(0)
