import codecs
hex='72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
print(b64)
# referred to https://stackoverflow.com/questions/33704327/hex-to-base64-conversion-in-python
#crypto/Base+64+Encoding+is+Web+Safe/

