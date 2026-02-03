import string
import random

def generate_password(length=12):
    #our character pool
    chars = string.ascii_letters + string.digits + string.punctuation

    # Pick random choice characters 'length' times
    password = ''.join(random.choice(chars) for _ in range(length))
    return password