import hashlib

def hash_password_without_salt(password: str)-> str:
    hash_password = hashlib.sha256(password.encode())
    return hash_password
