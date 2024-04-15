import sys
from cryptography.fernet import Fernet
# from key_operations import generated_key,save_key,load_key
# from file_operations import encrypt_file,decrypt_file
import os
from operations.file_operations import encrypt_file,decrypt_file
from operations.key_operations import generated_key,save_key,load_key
from operations.ascii import ascii




def main():
        try:
            ascii()
            while True:
                if len(sys.argv) != 2:
                    print("Usage: python3 encryption.py <file_name>")
                    sys.exit(1)
                filecheck=sys.argv[1]

                if not os.path.exists(filecheck):
                    print(f"Error: File '{filecheck}' not found.")
                    sys.exit(1)
                    
                else:
                    fileName = sys.argv[1]
                    choice = input("Do you want to encrypt (e) or decrypt (d) the file? ")

                    if choice.lower() == 'e':
                        key = generated_key()
                        print("Here is your encryption key: " + key.decode())
                        save_key(key)
                        encrypt_file(fileName,key)
                        print("Encryption Complete")

                    elif choice.lower() == 'd':
                        if os.path.exists('newkey.key'):
                            key = generated_key()
                            print("Here is your encryption key: " + key.decode())
                            key= load_key()
                            decrypt_file(fileName,key)
                            print("Encryption Complete")
                            os.remove("newkey.key")
                        else:
                            print("Error: 'newkey.key' not found. Please generate a key first bye encrypting.")
                        sys.exit(1)
                    else:
                        print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")
        except KeyboardInterrupt:
            print("\nYou stopped the Program")
            sys.exit(0)

if __name__ == "__main__":
    main()




