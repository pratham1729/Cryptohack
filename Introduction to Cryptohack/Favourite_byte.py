from pwn import xor

a=bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
arr=[byte for byte in a]
 
for i in range(256):
   x=[xor(i,b) for b in arr]
   flag_test="".join((j.decode() for j in x))
   if flag_test.startswith("crypto"):
       print(flag_test)
       break
