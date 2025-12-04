# import time, random

# # RNG Benchmark: how fast can Python generate random numbers?
# def benchmark_rng(count: int = 100_000):
#     print(f"--- Benchmarking RNG: generating {count} values ---")
#     start = time.time()
#     for _ in range(count):
#         random.random()
#     end = time.time()
#     elapsed = end - start
#     print(f"Time: {elapsed:.6f} sec ({count/elapsed:.2f} values/sec)")
#     return elapsed

# # Brute force seed recovery
# def brute_force_rng(target_value: float, tolerance: float = 1e-6, max_seed: int = 1_000_000):
#     print("\n--- Starting brute force seed search ---")
#     for seed in range(max_seed):
#         random.seed(seed)
#         if abs(random.random() - target_value) < tolerance:
#             print(f"Match found! Seed = {seed}")
#             return seed
#     print("No matching seed found.")
#     return None


# if __name__ == "__main__":
#     benchmark_rng(100000)

#     random.seed(12345)
#     target = random.random()

#     brute_force_rng(target, tolerance=1e-9, max_seed=2_000_000)