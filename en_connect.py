from Crypto.Cipher import AES


def crypto_this(input_plain, key_text, iv_text):
    input_b = input_plain.encode()
    key_text_b = key_text.encode()
    iv_text_b = iv_text.encode()
    obj_en = AES.new(key_text_b, AES.MODE_OFB, iv_text_b)
    to_encrypt = obj_en.encrypt(input_b)
    return to_encrypt


def decrypto_this(input_crypto, key_text, iv_text):
    input_b = input_crypto
    key_text_b = key_text.encode()
    iv_text_b = iv_text.encode()
    obj_de = AES.new(key_text_b, AES.MODE_OFB, iv_text_b)
    to_decrypt = obj_de.decrypt(input_b)
    return to_decrypt.decode("utf-8")

stored_info = "test_user, test_db, password"
key = "This is a key123"
iv = "This is an IV456"
encrypted_text = crypto_this(stored_info, key, iv)
print(encrypted_text)
decrypted_text = decrypto_this(encrypted_text, key, iv)
print(decrypted_text)
