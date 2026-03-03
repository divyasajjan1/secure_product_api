from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

load_dotenv()

# Get the key from your .env file
# Generated via: Fernet.generate_key()
ENCRYPTION_KEY = os.getenv("FIELD_ENCRYPTION_KEY").encode()
cipher_suite = Fernet(ENCRYPTION_KEY)

def encrypt_value(value):
    if value is None: return None
    return cipher_suite.encrypt(str(value).encode()).decode()

def decrypt_value(ciphertext):
    if ciphertext is None: return None
    return cipher_suite.decrypt(ciphertext.encode()).decode()