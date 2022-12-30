from pwn import xor
a= bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313") #KEY1
b= bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e") #KEY2 ^ KEY1 
c= bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1") #KEY2 ^ KEY3 
d= bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf") #FLAG ^ KEY1 ^ KEY3 ^ KEY2

k1=a
k2=xor(a,b)
k3=xor(c,k2)
flag=xor(d,k1,k2,k3)
print(flag)
