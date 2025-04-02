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
k = 0.5  # Conductividad térmica (W/m·K)
x1, x2 = 0, 2  # Posiciones inicial y final (m)

def dT_dx(x):
    """Derivada de la función de temperatura T(x) = 300 - 50x²"""
    return -100 * x  # Derivada de T(x)

# Solución analítica exacta
def flujo_exacto():
    return k * (T(x1) - T(x2))  # Ley de Fourier: Q = k·ΔT

def T(x):
    return 300 - 50*x**2

exact_value = flujo_exacto()
print(f"Flujo de calor exacto: {exact_value:.6f} W\n")

# Valores de n a probar
n_values = [6, 10, 20, 30]
results = []

for n in n_values:
    integral, x_vals, y_vals = simpson_rule(dT_dx, x1, x2, n)
    Q = -k * integral  # El signo negativo corrige la dirección del flujo
    error = abs(Q - exact_value)
    results.append((n, Q, error))
    print(f"n = {n}: Flujo ≈ {Q:.6f} W, Error = {error:.4e} W")

# Gráfica del gradiente de temperatura y puntos de evaluación (n=10)
n_plot = 10
_, x_plot, y_plot = simpson_rule(dT_dx, x1, x2, n_plot)
x_fine = np.linspace(x1, x2, 100)
dT_dx_fine = dT_dx(x_fine)

plt.figure(figsize=(12, 6))
plt.plot(x_fine, dT_dx_fine, 'b-', label=r'$\frac{dT}{dx} = -100x$')
plt.fill_between(x_fine, dT_dx_fine, alpha=0.2, color='blue')
plt.plot(x_plot, y_plot, 'ro', label=f'Puntos de evaluación (n={n_plot})')
plt.xlabel('Posición (m)')
plt.ylabel('Gradiente de temperatura (K/m)')
plt.title('Gradiente de temperatura y puntos de integración')
plt.legend()
plt.grid()
plt.savefig('gradiente_temperatura.png')
plt.show()

# Gráfica de convergencia
plt.figure(figsize=(10, 6))
n_list = [r[0] for r in results]
error_list = [r[2] for r in results]
plt.semilogy(n_list, error_list, 'bo-')
plt.xlabel('Número de subintervalos (n)')
plt.ylabel('Error absoluto (W)')
plt.title('Convergencia de la regla de Simpson para el cálculo del flujo de calor')
plt.grid()
plt.savefig('convergencia_flujo_calor.png')
plt.show()