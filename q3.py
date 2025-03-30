import numpy as np
from scipy.interpolate import CubicHermiteSpline
from scipy.optimize import minimize

# T,D,V
time_points = np.array([0, 3, 5, 8, 13])
distances = np.array([0, 200, 375, 620, 990])
speeds = np.array([75, 77, 80, 74, 72])


hermite_spline = CubicHermiteSpline(time_points, distances, speeds)

# a. 
t_predict = 10
position_at_10 = hermite_spline(t_predict)
speed_at_10 = hermite_spline.derivative()(t_predict)


# b. 
speed_limit_ft_s = 55 * 5280 / 3600  # 80.67ft/s

t_dense = np.linspace(0, 13, 1000)
speeds_dense = hermite_spline.derivative()(t_dense)


exceeds_limit_indices = np.where(speeds_dense > speed_limit_ft_s)[0]

first_exceed_idx = exceeds_limit_indices[0]
first_exceed_time = t_dense[first_exceed_idx]
   

# c. 找最大速度
def negative_speed(t):
    return -hermite_spline.derivative()(t)

optimization_result = minimize(negative_speed, 5, bounds=[(0, 13)])
max_speed_time = optimization_result.x[0]
max_speed = hermite_spline.derivative()(max_speed_time)

print(f"a. when t = 10: position = {position_at_10:.2f}ft, speed = {speed_at_10:.2f}ft/s")
print(f"b. The First time that vehicle reached 55 mile t = {first_exceed_time:.2f}s")
print(f"c. maximum speed is {max_speed:.2f}ft/s({max_speed * 3600 / 5280:.2f}mile/hr), when t = {max_speed_time:.2f}s")
