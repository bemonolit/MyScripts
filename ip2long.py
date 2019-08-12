#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
    print('You must use an IPv4 address as input...')
    sys.exit(1) 

IP = sys.argv[1]
IP = IP.split('.')
IP = list(map(int, IP))
LongIP = IP[0]*2**24 + IP[1]*2**16 + IP[2]*2**8 + IP[3]

print("IP as long format:")
print(LongIP)
