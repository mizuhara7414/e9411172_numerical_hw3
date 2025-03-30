import numpy as np
from scipy.interpolate import lagrange

#  (x, f(x))
x_vals = np.array([0.3, 0.4, 0.5, 0.6])  # x 值
y_vals = x_vals - np.exp(-x_vals)  #  f(x) = x - e^(-x)

# 目標 f(x) = 0
y_target = 0.0

# 線性
x1, x2 = x_vals[2], x_vals[3]  #  (x=0.5, x=0.6)
y1, y2 = y_vals[2], y_vals[3]

# 線性
x_linear = x1 + (y_target - y1) * (x2 - x1) / (y2 - y1)

print(f"Linear inverse interpolation x ≈ {x_linear:.6f}")

# 二次
poly = lagrange(y_vals[1:], x_vals[1:])  # x=0.4, 0.5, 0.6 
x_quadratic = poly(y_target)

print(f"Quadratic inverse interpolation x ≈ {x_quadratic:.6f}")

x_real = 0.56714329  
print(f"True solution x = {x_real:.6f}")

# 誤差
error_linear = abs(x_real - x_linear)
error_quadratic = abs(x_real - x_quadratic)

print(f"Error in linear interpolation: {error_linear:.6e}")
print(f"Error in quadratic interpolation: {error_quadratic:.6e}")

