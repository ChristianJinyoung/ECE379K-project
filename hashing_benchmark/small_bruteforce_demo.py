import time
import hashlib
import bcrypt
from argon2 import PasswordHasher

TARGET_PASSWORD = "1234"

TARGET_HASH_SHA = hashlib.sha256(TARGET_PASSWORD.encode()).hexdigest()

TARGET_HASH_BCRYPT = bcrypt.hashpw(TARGET_PASSWORD.encode(), bcrypt.gensalt(10))

argon = PasswordHasher(time_cost=2, memory_cost=102400, parallelism=8)
TARGET_HASH_ARGON = argon.hash(TARGET_PASSWORD)

SCRYPT_N = 2**14
SCRYPT_R = 8
SCRYPT_P = 1
SCRYPT_DKLEN = 64

TARGET_HASH_SCRYPT = hashlib.scrypt(
    TARGET_PASSWORD.encode(),
    salt=b"fixed_salt_1234",
    n=SCRYPT_N,
    r=SCRYPT_R,
    p=SCRYPT_P,
    dklen=SCRYPT_DKLEN
)

def brute_force_sha256():
    print("\n[+] Starting SHA-256 brute force (0000–9999)...")
    start = time.time()

    for i in range(10000):
        guess = f"{i:04d}"
        if hashlib.sha256(guess.encode()).hexdigest() == TARGET_HASH_SHA:
            end = time.time()
            return guess, end - start

    return None, None


def brute_force_bcrypt():
    print("\n[+] Starting bcrypt brute force (0000–9999)...")
    start = time.time()

    for i in range(10000):
        guess = f"{i:04d}"
        if bcrypt.checkpw(guess.encode(), TARGET_HASH_BCRYPT):
            end = time.time()
            return guess, end - start

    return None, None


def brute_force_argon2():
    print("\n[+] Starting Argon2id brute force (0000–9999)...")
    start = time.time()

    for i in range(10000):
        guess = f"{i:04d}"
        try:
            argon.verify(TARGET_HASH_ARGON, guess)
            end = time.time()
            return guess, end - start
        except:
            pass

    return None, None


def brute_force_scrypt():
    print("\n[+] Starting scrypt brute force (0000–9999)...")
    start = time.time()

    for i in range(10000):
        guess = f"{i:04d}"
        test_hash = hashlib.scrypt(
            guess.encode(),
            salt=b"fixed_salt_1234",
            n=SCRYPT_N,
            r=SCRYPT_R,
            p=SCRYPT_P,
            dklen=SCRYPT_DKLEN
        )

        if test_hash == TARGET_HASH_SCRYPT:
            end = time.time()
            return guess, end - start

    return None, None


if __name__ == "__main__":
    print("=== Small Keyspace Brute-Force Demo (4-digit PIN) ===")

    guess, t = brute_force_sha256()
    print(f"SHA-256 cracked PIN: {guess} in {t:.6f} seconds")

    guess, t = brute_force_bcrypt()
    print(f"bcrypt cracked PIN: {guess} in {t:.2f} seconds")

    guess, t = brute_force_argon2()
    print(f"Argon2id cracked PIN: {guess} in {t:.2f} seconds")

    guess, t = brute_force_scrypt()
    print(f"scrypt cracked PIN: {guess} in {t:.2f} seconds")
