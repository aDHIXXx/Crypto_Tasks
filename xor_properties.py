k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k2k3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flagk1k2k3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
x=''
k1_ord = [o for o in bytes.fromhex(k1)]
k2k3_ord = [o for o in bytes.fromhex(k2k3)]
flagk1k2k3_ord = [o for o in bytes.fromhex(flagk1k2k3)]
for i in range(len(k1_ord)):
     x=x+chr((k1_ord[i])^(k2k3_ord[i])^(flagk1k2k3_ord[i]))
print(x)
     

