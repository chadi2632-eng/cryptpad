data = bytes.fromhex("""
c9 98 8f c7 a6 1c 02 6b e2 06 f3 52 49 16 27 59
45 5c 4c 47 bc 4e 28 a6 2f 71 c7 d8 06 85 42 03
08 50 7d 93 f5 fe e5 99 48 4e 82 2b e2 00 57 26
16 f6 b4 1c
""")
s=list(range(256))
j=0
rc4_key=bytes.fromhex("E8 17 1B F4 50 3F 3D 70")
for i in range(256):
    j=(j+s[i]+rc4_key[i%8]) & 0xff
    s[i],s[j]=s[j],s[i]

i=j=0
result=[]
for byte in data:
    
    i=(i+1)&0xff
    j=(j+s[i])&0x0ff
    s[i],s[j]=s[j],s[i]
    k=s[(s[i]+s[j])&0xff]
    result.append(k^byte)


print(bytes(result).decode(errors="ignore"))

