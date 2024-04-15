from cryptography.fernet import Fernet

def generated_key():
    return Fernet.generate_key()

def save_key(key):
    with open('newkey.key' ,'wb') as filekey:
        filekey.write(key)

def load_key():
    with open('newkey.key', 'rb') as filekey:
        return filekey.read()