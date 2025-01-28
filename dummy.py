# dummy me needs a program to bootstrap my new application

import secrets
#import base64
from passlib.context import CryptContext


# Input parameters and constants
#pepper = secrets.token_hex(512) # random 512 character string
salting = secrets.token_hex(32)    # random 32 character string
#seed = secrets.token_hex(1024)  # random 1024 character string
user = "UserName"
passing = '&H!%ist0osh0rt4ap45sw0rd'
app_iter = int(25)

#arg_varient = 'id'  # Varients available are 'i' 'd' 'id'
#arg_version = '19'  # Version code 19 is for Argon 1.3
arg_m = '25165824'  # 24 MiB value in KiB (47104 (46 MiB), 19456 (19 MiB)** (OWASP recommened minimum))
#arg_t = '1'         # integer representing the variable time cost
#arg_p = '1'         # parallelization parameter
#arg_s = '1024'      # Salt - this is the base64-encoded version of the raw salt bytes(length must be between 0-1024 bytes)
#arg_d = '128'          # size of the digest to output (i.e., 16, 32, 64, 128, 196, 256, etc)

# PBKDF function using Argon2
# Define a more complex context
ctx = CryptContext(
    schemes="argon2",
    argon2__time_cost=4,
    argon2__memory_cost=25165824,
    argon2__parallelism=1
)

hashed_pass = ctx.hash("&H!%ist0osh0rt4ap45sw0rd")

#with open('.App/start.bin', '+a') as fd:
#    fd.write(hb)

#fd.flush()
#fd.close()

print(hashed_pass)
# print('\n')
# print(h.digest_bits)