# dummy me needs a program to bootstrap my new application
# this program will create the initial security framework for starting the StratHunter 
# application for the first time.

import secrets
from passlib.context import CryptContext


# Input parameters and constants
#pepper = secrets.token_hex(512) # random 512 character string
salting = secrets.token_hex(32)    # random 32 character string
#seed = secrets.token_hex(1024)  # random 1024 character string
user = "UserName"
passing = '&H!%ist0osh0rt4ap45sw0rd'
arg_m = '25165824'  # 24 MiB value in KiB (47104 (46 MiB), 19456 (19 MiB)** (OWASP recommened minimum))

# Define a more complex context
ctx = CryptContext(
    schemes="argon2",
    argon2__time_cost=4,
    argon2__memory_cost=25165824,
    argon2__parallelism=1
)

hashed_pass = ctx.hash("&H!%ist0osh0rt4ap45sw0rd")

print(hashed_pass)
