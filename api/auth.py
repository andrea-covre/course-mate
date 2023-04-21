import os
import hashlib
from dotenv import load_dotenv

load_dotenv()
HASHED_API_TOKEN = os.getenv("HASHED_API_TOKEN")

def __hash_token(token):
    hash_object = hashlib.sha256()
    encoded_token = token.encode('utf-8')
    hash_object.update(encoded_token)
    hex_dig = hash_object.hexdigest()
    return hex_dig

def authenticate(auth_token):
    return __hash_token(auth_token) == HASHED_API_TOKEN
