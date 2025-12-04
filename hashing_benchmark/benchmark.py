import time
import hashlib
import bcrypt
import argon2
import hashlib

def bench_sha256():
    start = time.time()
    for _ in range(10000):
        hashlib.sha256(b"password").hexdigest()
    end = time.time()
    return (end - start) / 10000 * 1000  # ms per hash

def bench_bcrypt(cost):
    total = 0
    for _ in range(10):
        start = time.time()
        bcrypt.hashpw(b"password", bcrypt.gensalt(rounds=cost))
        end = time.time()
        total += (end - start)
    return total / 10 * 1000

def bench_scrypt():
    total = 0
    for _ in range(10):
        start = time.time()
        hashlib.scrypt(
            b"password",
            salt=b"saltsalt",
            n=2**14,
            r=8,
            p=1
        )
        total += (time.time() - start)
    return total / 10 * 1000

def bench_argon2():
    ph = argon2.PasswordHasher(
        time_cost=2,
        memory_cost=65536,   # 64 MB
        parallelism=2
    )
    total = 0
    for _ in range(10):
        start = time.time()
        ph.hash("password")
        total += (time.time() - start)
    return total / 10 * 1000

print("SHA256:", bench_sha256(), "ms")
print("bcrypt cost=10:", bench_bcrypt(10), "ms")
print("scrypt:", bench_scrypt(), "ms")
print("argon2:", bench_argon2(), "ms")
