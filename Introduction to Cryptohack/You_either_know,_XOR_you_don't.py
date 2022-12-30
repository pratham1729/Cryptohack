from pwn import xor

a=bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
arr=[byte for byte in a]
crypto=[ord(i) for i in "crypto{}"]
k=[]
k.append(arr[0]^crypto[0])
k.append(arr[1]^crypto[1])
k.append(arr[2]^crypto[2])
k.append(arr[3]^crypto[3])
k.append(arr[4]^crypto[4])
k.append(arr[5]^crypto[5])
k.append(arr[6]^crypto[6])
k.append(arr[-1]^crypto[-1])

final=[]
for i in range(1,len(arr)+1):
    final.append(arr[i-1]^k[(i-1)%8])
ans="".join((chr(j) for j in final))
print(ans)
