#!/usr/bin/python3
import sys

if len(sys.argv) < 3:
    print('\nYou must give desired format and IPv4 address as input...')
    print('e.g.: D 192.168.10.100')
    print('Valid formats D=Decimal H=Hexadecimal\n')
    sys.exit(1)

Format = sys.argv[1]

def long(ip):
   #IP = sys.argv[2]
   IP = ip.split('.')
   IP = list(map(int, IP))
   LongIP = IP[0]*2**24 + IP[1]*2**16 + IP[2]*2**8 + IP[3]
   return LongIP

if Format == 'D':
   Lip = long(sys.argv[2])
   print('\nIP as Decimal format:')
   print(Lip)

if Format == 'H':
   Hip = long(sys.argv[2])
   Hip = hex(Hip)
   print('\nIP as Hexadecimal format:')
   print(Hip)
