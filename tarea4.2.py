import numpy as np
import matplotlib.pyplot as plt

def simpson_rule(f, a, b, n):
    """Aproxima la integral de f(x) en [a, b] usando la regla de Simpson."""
    if n % 2 == 1:
        n += 1  # Asegura que n sea par
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = f(x)
    integral = (h / 3) * (fx[0] + 4*np.sum(fx[1:n:2]) + 2*np.sum(fx[2:n-1:2]) + fx[n])
    return integral, x, fx

# Parámetros del problema
C = 1e-6  # Capacitancia (1 μF)
T = 5     # Tiempo final (5 segundos)
def V(t):
    return 100 * np.exp(-2*t)  # Voltaje en función del tiempo

# Solución analítica exacta
def carga_exacta():
    return C * 100 * (1 - np.exp(-2*T)) / 2

exact_value = carga_exacta()
print(f"Carga exacta: {exact_value:.10f} C\n")

# Valores de n a probar
n_values = [6, 10, 20, 30]
results = []

for n in n_values:
    integral, x_vals, y_vals = simpson_rule(V, 0, T, n)
    Q = C * integral
    error = abs(Q - exact_value)
    results.append((n, Q, error))
    print(f"n = {n}: Carga ≈ {Q:.10f} C, Error = {error:.4e} C")

# Gráfica del voltaje y puntos de evaluación (n=10)
n_plot = 10
_, x_plot, y_plot = simpson_rule(V, 0, T, n_plot)
t_fine = np.linspace(0, T, 100)
V_fine = V(t_fine)

plt.figure(figsize=(12, 6))
plt.plot(t_fine, V_fine, 'b-', label=r'$V(t) = 100e^{-2t}$ V')
plt.fill_between(t_fine, V_fine, alpha=0.2, color='blue')
plt.plot(x_plot, y_plot, 'ro', label=f'Puntos de evaluación (n={n_plot})')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.title('Voltaje en el capacitor y puntos de integración')
plt.legend()
plt.grid()
plt.savefig('voltaje_capacitor.png')
plt.show()

# Gráfica de convergencia
plt.figure(figsize=(10, 6))
n_list = [r[0] for r in results]
error_list = [r[2] for r in results]
plt.semilogy(n_list, error_list, 'bo-')
plt.xlabel('Número de subintervalos (n)')
plt.ylabel('Error absoluto (C)')
plt.title('Convergencia de la regla de Simpson para el cálculo de Q')
plt.grid()
plt.savefig('convergencia_carga.png')
plt.show()