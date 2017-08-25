from Crypto.Cipher import AES
obj = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')
message=b'The answer is no'
ciphertext = obj.encrypt(message)
print(ciphertext)
obj2 = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')
print(obj2.decrypt(ciphertext))
