import time
import hashlib
import bcrypt
import argon2

def time_per_sha():
    start = time.time()
    for _ in range(500000):
        hashlib.sha256(b"password").hexdigest()
    return (time.time() - start) / 500000

def time_per_bcrypt():
    start = time.time()
    bcrypt.hashpw(b"password", bcrypt.gensalt(rounds=10))
    return time.time() - start

def time_per_argon2():
    ph = argon2.PasswordHasher()
    start = time.time()
    ph.hash("password")
    return time.time() - start

lowercase = 26
digits = 10
charset = lowercase + digits

def estimate_bruteforce(time_per_hash, length):
    total = charset ** length
    seconds = total * time_per_hash
    return seconds

print("SHA256 per hash:", time_per_sha())
print("bcrypt per hash:", time_per_bcrypt())
print("argon2 per hash:", time_per_argon2())
