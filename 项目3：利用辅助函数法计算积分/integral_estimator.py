import numpy as np


def generate_random_numbers(N):
    return np.random.rand(N)


def estimate_integral(N):
    x = np.random.rand(N)
    return np.sum(1 / np.sqrt(x) / (np.exp(x) + 1)) / N


def estimate_error(N, integral_estimate):
    x = np.random.rand(N)
    f = 1 / np.sqrt(x) / (np.exp(x) + 1)
    f_squared = f ** 2
    var_f = np.mean(f_squared) - np.mean(f) ** 2
    return np.sqrt(var_f / N)


if __name__ == "__main__":
    N = 1000000
    random_numbers = generate_random_numbers(N)
    integral_estimate = estimate_integral(N)
    error_estimate = estimate_error(N, integral_estimate)
    print("Integral estimate:", integral_estimate)
    print("Estimated error:", error_estimate)
