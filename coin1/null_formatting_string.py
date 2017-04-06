#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *
from struct import pack, unpack
from sys import *


# count = 0
conn = remote("pwnable.kr", 9007)
# conn = process('./format1_32')


# Welcome message
# front_line = conn.recvuntil("\n")


conn.recvuntil("Ready? starting in 3 sec... -")
conn.recv()
while 1:
    cas = conn.recv()
    print cas
    npb = cas.index("N=")
    n = int(cas[npb + 2: cas.index(" ")])
    # print n
    c = int(cas[cas.index("C=") + 2: cas.index("\n")])
    # print c


    fuck = c
    l = 1
    h = n
    while 1:
        c -= 1;
        if c == -1:
            # print "we are sending", str(h)
            conn.sendline(str(h))
            conn.recvline()

            # print "what fucking"
            break

        if h == l:
            # print "we are sending", str(h)
            conn.sendline(str(h))
            conn.recvline()
            continue
        mid = (l + h) /2
        tmp = ""
        for i in range(l, mid + 1):
            tmp += " " + str(i)
        conn.sendline(tmp)
        t = conn.recvline()
        all_ = (mid - l + 1) * 10
        # print int(t) , " ", all_
        # print l, h
        if all_ == int(t):
            l = mid+1
        else:
            h = mid





    # print conn.recv()
    # print conn.recvuntil("\n")

# # payload = "A"+ p32(addr) + "%13$0251c" + "%7$hhn"
# payload =   b'\x11\x11\x11\x11'*13+b'\xbe\xba\xfe\xca'
#
# # payload = "B" + p32(addr) + "%08x.%08x.%08x.%08x.%08x.%n"
# print len(payload)
#
# log.info('Sending payload:' + payload)
# conn.sendline(payload)
# conn.interactive()
# print conn.recvall()
# conn.close()
