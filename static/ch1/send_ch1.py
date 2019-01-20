#!/usr/bin/python3

#Send a ICMP message in loop, wi²th the flag in payload
#   input : IP dest
#   Flag file has to be ./flag.txt

from scapy.all import *
import sys
import re
import time

def testIP(ip):
    regex = "^(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})$"

    if (ip is None):
        return -1
    result = re.match(regex, ip)
    if (result is None):
        return -1
    else:
        for i in range(1,5):
            if (int(result.group(i)) >= 255):
                return -1
    return 0


file = open('flag.txt')
flag = file.read()
if len(sys.argv) !=2:
    print("usage")
    exit(1)
ip = sys.argv[1]
if(testIP(ip)):
    exit(1)


payload="flag="+flag
send(IP(dst=ip)/ICMP()/payload, loop=1, inter=5.0)


