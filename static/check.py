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

uans=argv[1]
ans=open('.answer.txt')

if uans == ans:
    flag=open("flag")
    print("Congratulation ! The flag is : "+flag+" \n")
else:
    print("Sorry, wrong answer.. keep trying  !")
