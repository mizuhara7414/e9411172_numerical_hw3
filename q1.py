import numpy as np
from scipy.interpolate import lagrange


x_vals = np.array([0.698, 0.733, 0.768, 0.803])
y_vals = np.array([0.7661, 0.7432, 0.7193, 0.6946])


x_target = 0.750


p1 = lagrange(x_vals[:2], y_vals[:2])  
p2 = lagrange(x_vals[:3], y_vals[:3]) 
p3 = lagrange(x_vals[:4], y_vals[:4])  
p4 = lagrange(x_vals,y_vals)

p1_val = p1(x_target)
p2_val = p2(x_target)
p3_val = p3(x_target)
p4_val = p4(x_target)



print(f"degree 1 interpolation P1(0.750) = {p1_val:.6f}")
print(f"degree 2 interpolation P2(0.750) = {p2_val:.6f}")
print(f"degree 3 interpolation P3(0.750) = {p3_val:.6f}")
print(f"degree 4 interpolation P4(0.750) = {p4_val:.6f}")  


real_value = np.cos(0.750)


error_p1 = abs(real_value - p1_val)
error_p2 = abs(real_value - p2_val)
error_p3 = abs(real_value - p3_val)
error_p4 = abs(real_value - p4_val)

print(f"real value cos(0.750) = {real_value:.6f}")
print(f"Error for P1: {error_p1:.6e}")
print(f"Error for P2: {error_p2:.6e}")
print(f"Error for P3: {error_p3:.6e}")
print(f"Error for P4: {error_p4:.6e}") 
