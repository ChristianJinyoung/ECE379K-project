import tracemalloc
import hashlib
import argon2

def measure_memory(func):
    tracemalloc.start()
    func()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / (1024 * 1024)

def run_scrypt():
    hashlib.scrypt(b"password", salt=b"saltsalt", n=2**14, r=8, p=1)

def run_argon2():
    ph = argon2.PasswordHasher(
        time_cost=2,
        memory_cost=65536,
        parallelism=2
    )
    ph.hash("password")

print("scrypt peak MB:", measure_memory(run_scrypt))
print("argon2 peak MB:", measure_memory(run_argon2))
