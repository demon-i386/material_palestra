from pwn import *

elf = ELF("./overflow")

p = process("./overflow")
p.sendline(cyclic(200, n=8))
p.wait()

core = p.corefile

print(cyclic_find(core.read(core.rsp, 8), n=8))
