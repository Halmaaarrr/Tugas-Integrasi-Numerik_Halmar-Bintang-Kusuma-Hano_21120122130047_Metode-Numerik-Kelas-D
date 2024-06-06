import numpy as np
import timeit
import matplotlib.pyplot as plt

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Implementasi Metode Simpson 1/3
def simpson_1_3(f, a, b, N):
    if N % 2 == 1:
        raise ValueError("N harus genap untuk metode Simpson 1/3")
    
    h = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    
    S = y[0] + y[-1]
    
    for i in range(1, N, 2):
        S += 4 * y[i]
    for i in range(2, N-1, 2):
        S += 2 * y[i]
    
    return (h / 3) * S

# Fungsi untuk menghitung galat RMS
def rms_error(approx, exact):
    return np.sqrt(np.mean((approx - exact)**2))

# Fungsi untuk melakukan pengujian dengan timeit
def test_simpson(N_values, exact_value):
    results = []
    for N in N_values:
        timer = timeit.Timer(lambda: simpson_1_3(f, 0, 1, N))
        elapsed_time = timer.timeit(number=10) / 10  # rata-rata waktu dari 10 eksekusi
        approx_pi = simpson_1_3(f, 0, 1, N)
        error = rms_error(approx_pi, exact_value)
        results.append((N, approx_pi, error, elapsed_time))
    return results

# Nilai referensi untuk π
exact_pi = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Melakukan pengujian
results = test_simpson(N_values, exact_pi)

# Menampilkan hasil pengujian dalam bentuk tabel
for N, approx_pi, error, elapsed_time in results:
    print(f"N = {N}, Approximation of π = {approx_pi}, RMS Error = {error}, Execution Time = {elapsed_time:.10f} seconds")

# Menampilkan hasil pengujian dalam bentuk grafik
N_values = [result[0] for result in results]
approx_values = [result[1] for result in results]
errors = [result[2] for result in results]
times = [result[3] for result in results]

# Plotting Approximation of π
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(N_values, approx_values, 'o-', label='Approximation of π')
plt.axhline(y=exact_pi, color='r', linestyle='--', label='Exact π')
plt.xlabel('N')
plt.ylabel('Approximation of π')
plt.legend()
plt.title('Approximation of π vs N')

# Plotting RMS Error
plt.subplot(1, 3, 2)
plt.plot(N_values, errors, 's-', label='RMS Error')
plt.xlabel('N')
plt.ylabel('RMS Error')
plt.legend()
plt.title('RMS Error vs N')

# Plotting Execution Time
plt.subplot(1, 3, 3)
plt.plot(N_values, times, 'x-', label='Execution Time')
plt.xlabel('N')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.title('Execution Time vs N')

plt.tight_layout()
plt.show()
