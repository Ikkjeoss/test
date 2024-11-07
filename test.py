from cryptography.fernet import Fernet

# Function to generate and write a key to a file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key from a file
def load_key():
    return open("key.key", "rb").read()

# Function to encrypt a file
def encrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)
    
    with open(file_name, "rb") as file:
        file_data = file.read()
    
    encrypted_data = fernet.encrypt(file_data)
    
    with open(file_name, "wb") as file:
        file.write(encrypted_data)

# Function to decrypt a file
def decrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)
    
    with open(file_name, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    with open(file_name, "wb") as file:
        file.write(decrypted_data)

# Example usage remove the # to decrypt the file and put # to encrypt_file
write_key()  # Generate and write a new key
encrypt_file("example.txt")  # Encrypt the file
#decrypt_file("example.txt")  # Decrypt the file

