x='73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
x1= [o for o in bytes.fromhex(x)]
key=16 #for i in range(1,1000):
       #     if 99^i==115:
       #          print(i) ---> This i is key
check=''
for i in range(1,len(x1)):
   check=check+chr((x1[i])^key) 
print(check)

