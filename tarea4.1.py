import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_rule(f, a, b, n):
    """Aproxima la integral de f(x) en [a, b] usando la regla del trapecio."""
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)  # Puntos del intervalo
    fx = f(x)  # Evaluamos la función en esos puntos
    
    # Regla del trapecio
    integral = (h / 2) * (fx[0] + 2 * np.sum(fx[1:n]) + fx[n])
    return integral, x, fx

# Función del resorte: F(x) = kx
def fuerza_resorte(x):
    k = 200  # Constante del resorte en N/m
    return k * x

# Parámetros del problema
a, b = 0.1, 0.3  # Posiciones inicial y final en metros
n_values = [6, 10, 20, 30]  # Valores de n a probar

# Solución analítica exacta
def trabajo_exacto(a, b):
    k = 200
    return 0.5 * k * (b**2 - a**2)

exact_value = trabajo_exacto(a, b)
print(f"Trabajo exacto: {exact_value:.4f} J\n")

# Resultados para diferentes n
results = []
for n in n_values:
    integral_approx, x_vals, y_vals = trapezoidal_rule(fuerza_resorte, a, b, n)
    error = abs(integral_approx - exact_value)
    results.append((n, integral_approx, error))
    print(f"n = {n}: Trabajo ≈ {integral_approx:.4f} J, Error = {error:.6f} J")

# Gráfica de la función y las aproximaciones (para n=10 como ejemplo)
x_fine = np.linspace(a, b, 100)
y_fine = fuerza_resorte(x_fine)
n_plot = 10
integral_plot, x_plot, y_plot = trapezoidal_rule(fuerza_resorte, a, b, n_plot)

plt.figure(figsize=(10, 6))
plt.plot(x_fine, y_fine, 'k-', label='Fuerza del resorte (F(x) = 200x)', linewidth=2)
plt.fill_between(x_plot, y_plot, alpha=0.3, color='blue', label="Aproximación del trabajo")
plt.plot(x_plot, y_plot, 'ro-', label=f"Puntos de evaluación (n={n_plot})")
plt.xlabel("Desplazamiento (m)")
plt.ylabel("Fuerza (N)")
plt.title("Trabajo realizado por el resorte (Regla del Trapecio)")
plt.legend()
plt.grid()
plt.savefig("trabajo_resorte.png")
plt.show()

# Gráfica de error vs número de subintervalos
plt.figure(figsize=(8, 5))
n_list = [r[0] for r in results]
error_list = [r[2] for r in results]
plt.plot(n_list, error_list, 'bo-')
plt.xlabel("Número de subintervalos (n)")
plt.ylabel("Error absoluto (J)")
plt.title("Convergencia del método del trapecio")
plt.grid()
plt.savefig("convergencia_trapecio_resorte.png")
plt.show()