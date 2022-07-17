from pwn import *

conn = remote('vm2.gabrielseet.com', 1342)
conn.recvline()
