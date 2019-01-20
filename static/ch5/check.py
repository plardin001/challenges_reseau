#!/usr/bin/python3

#Check the data found by the player and return the flag if success
#    no input.
#    require : flag in ./flag.txt


rIp1="46.51.179.90"
rIp2="79.125.105.113"
rIp3="176.34.155.23"
rMX1="in1-smtp.messagingengine.com"

ans1 = input("Is there an IPv6 address in the DNS record ? [y/n] : ")
Ipv6 = str(ans1)

if Ipv6 != 'n' and Ipv6 != 'N' and Ipv6 != 'no' and  Ipv6 != 'No' and Ipv6 != 'NO':
    print("Sorry, keep trying")
    exit(1)

else:
    print("Well done !")
    ans2 = input("Please now enter one of the IPv4 address : ")
    ip= str(ans2)

    if ip != rIp1 and ip != rIp2 and ip != rIp3 :
        print("Sorry, keep trying")
        exit(1)

    else:
        print("You are doing well ! ")
        ans3=input("The last step: give the mail server with the highest priority : ")
        MX1=str(ans3)

        if MX1 != rMX1 and MX1 != rMX1+'.':
            print("Sorry, keep trying")
            exit(1)
        else:
            fd=open("flag.txt")
            flag=fd.read()
            print("Congratulation ! The flag is : "+flag+" \n")
            exit(0)
