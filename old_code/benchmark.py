# import time, os
# import hashlib
# import statistics
# import random
# import bcrypt
# from argon2 import PasswordHasher
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.hazmat.primitives import hashes

# # PBKDF2 Benchmark
# def benchmark_pbkdf2(iterations_list=[50_000, 100_000, 200_000]):
#     password = b"test_password"
#     salt = os.urandom(16)

#     print("\n===== PBKDF2 Benchmarks =====")
#     for iterations in iterations_list:
#         kdf = PBKDF2HMAC(
#             algorithm=hashes.SHA256(),
#             length=32,
#             salt=salt,
#             iterations=iterations,
#         )
#         start = time.time()
#         kdf.derive(password)
#         end = time.time()
#         print(f"Iterations: {iterations}, Time: {end - start:.4f} sec")


# #bcrypt Benchmark
# def benchmark_bcrypt():
#     print("\n===== bcrypt Benchmarks =====")
#     password = b"password123"

#     for cost in [10, 12, 14]:
#         start = time.time()
#         bcrypt.hashpw(password, bcrypt.gensalt(rounds=cost))
#         end = time.time()

#         print(f"bcrypt (cost={cost}): {1000*(end-start):.2f} ms")


# # Argon2 Benchmark
# def benchmark_argon2():
#     print("\n===== Argon2id Benchmarks =====")
#     ph = PasswordHasher()
#     password = "password123"

#     params = [
#         ("64MB", 65536, 2),
#         ("128MB", 131072, 2),
#         ("256MB", 262144, 3),
#     ]

#     for label, mem_kib, time_cost in params:
#         start = time.time()
#         ph.hash(password)
#         end = time.time()

#         print(f"Argon2id (m={label}, t={time_cost}): {1000*(end-start):.2f} ms")

# # scrypt Benchmark
# def benchmark_scrypt(N_values=[16384, 24576, 32768]):
#     password = b"test_password"
#     salt = os.urandom(16)

#     print("\n===== scrypt Benchmarks =====")
#     for N in N_values:
#         start = time.time()
#         try:
#             hashlib.scrypt(password, salt=salt, n=N, r=8, p=1)
#             end = time.time()
#             print(f"scrypt (N={N}): {(end - start) * 1000:.2f} ms")
#         except ValueError as e:
#             print(f"scrypt (N={N}): ERROR ({str(e)})")

# if __name__ == "__main__":
#     benchmark_pbkdf2()
#     benchmark_bcrypt()
#     benchmark_argon2()
#     benchmark_scrypt()
#     #benchmark_rng()  # optional

