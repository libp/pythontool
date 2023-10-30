from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def aes_encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    return base64.b64encode(ciphertext).decode('utf-8')

def aes_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(base64.b64decode(ciphertext))
    return unpad(decrypted_data, AES.block_size).decode('utf-8')

def ciphertext_to_hex(ciphertext):
    ciphertext_bytes = base64.b64decode(ciphertext)
    ciphertext_hex = ciphertext_bytes.hex().upper()
    return ciphertext_hex

def hex_to_ciphertext(hex_string):
    ciphertext_bytes = bytes.fromhex(hex_string)
    ciphertext = base64.b64encode(ciphertext_bytes).decode('utf-8')
    return ciphertext

# 加密
key = b'aaaaaaaaaaaaaaaa'
iv = b'1234567890123456'
plaintext = '{"confId":"11111"}'
ciphertext = aes_encrypt(plaintext, key, iv)
print("密文:", ciphertext)

# 密文转换为大写十六进制字符串
ciphertext_hex = ciphertext_to_hex(ciphertext)
print("密文的大写十六进制表示:", ciphertext_hex)

# 大写十六进制字符串转换为密文
ciphertext_restored = hex_to_ciphertext(ciphertext_hex)
print("还原后的密文:", ciphertext_restored)

# 解密
decrypted_text = aes_decrypt(ciphertext_restored, key, iv)
print("解密后的明文:", decrypted_text)
