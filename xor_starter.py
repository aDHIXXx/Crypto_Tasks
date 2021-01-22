string='label'
crypt=''
for x in string:
     crypt=crypt+(chr(ord(x)^13))
print(crypt)

