from Crypto.Cipher import AES
obj = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')
message='The answer is no'
b_message=message.encode()
ciphertext = obj.encrypt(b_message)
print(ciphertext)
obj2 = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')
my_password = ""
print(obj2.decrypt(ciphertext).decode("utf-8"))


def crypto_this(input_plain, key_text, salt_text):
    input_b = input_plain.encode()
    key_text_b = key_text.encode()
    salt_text_b = salt_text.encode()
    obj_en = AES.new(key_text_b, AES.MODE_OFB, salt_text_b)
    to_encrypt = obj_en.encrypt(input_b)
    return to_encrypt

encrypted_text = crypto_this("test_user, test_db, password", "This is a key123", "This is an IV456")
print(encrypted_text)
