from cryptography.fernet import Fernet

def encrypt_file(fileName, key):
    fernet= Fernet(key)
    with open(fileName, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(fileName, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file(fileName, key):
    fernet= Fernet(key)
    with open(fileName, 'rb') as file:
        encrypted_file = file.read()
    decrypted = fernet.decrypt(encrypted_file)
    with open(fileName, 'wb') as dec_file:
        dec_file.write(decrypted)
