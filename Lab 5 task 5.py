import string
from random import sample
def get_random_password() -> str:
    password = ''
    size = 8
    symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = "".join(sample(symbols, size))
    return password

print(get_random_password())
