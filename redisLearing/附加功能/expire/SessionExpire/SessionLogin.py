import random
from hashlib import sha256
DEFAULT_TIMEOUT = 3600 * 24 * 30
SESSION_NOT_LOGIN_OR_EXPIRED = "SESSION_NOT_LOGIN_OR_EXPIRED"
SESSION_TOKEN_CORRECT = "SESSION_TOKEN_CORRECT"
SESSION_TOKEN_INCORRECT = "SESSION_TOKEN_INCORRECT"

def generate_token():
    random_string = str(random.getrandbits(256)).encode("utf-8")
    return sha256(random_string).hexdigest()

class SessionLogin:
    def __init__(self, client,user_id) -> None:
        self.client = client
        self.user_id = user_id
        self.key = f"user::{user_id}::token"
    def create(self, timeout=DEFAULT_TIMEOUT):
        token = generate_token()
        self.client.set(self.key, token, ex=timeout)
        return token
    def validate(self, input_token):
        token = self.client.get(self.key)
        if token is None:
            return SESSION_NOT_LOGIN_OR_EXPIRED
        if token == input_token:
            return SESSION_TOKEN_CORRECT
        else:
            return SESSION_TOKEN_INCORRECT
    def destroy(self):
        self.client.delete(self.key)