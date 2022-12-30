def myxor(string, integer):
   result=""
   for i in string:
       result+=chr(ord(i) ^ integer)
   return result
print(myxor("label",13))