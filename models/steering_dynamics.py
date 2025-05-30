import numpy as np
import matplotlib.pyplot as plt

# Parameters
steering_ratio = 16  # ratio: steering wheel angle / road wheel angle
assist_gain = 1.2    # multiplier for motor assist

# Time array
t = np.linspace(0, 10, 500)  # 10 seconds, 500 samples

# Simulated driver input: steering wheel angle (degrees)
steering_wheel_angle = 10 * np.sin(0.5 * t)  # smooth sine wave input

# Road wheel angle (degrees)
road_wheel_angle = steering_wheel_angle / steering_ratio

# Assist torque (Nm)
driver_torque = 2 * np.sin(0.5 * t)  # driver applies 2 Nm sinusoidal torque
assist_torque = assist_gain * driver_torque

# Effective total torque
total_torque = driver_torque + assist_torque

# Plotting results
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, steering_wheel_angle)
plt.title("Steering Wheel Angle (degrees)")

plt.subplot(3, 1, 2)
plt.plot(t, road_wheel_angle)
plt.title("Road Wheel Angle (degrees)")

plt.subplot(3, 1, 3)
plt.plot(t, total_torque)
plt.title("Total Torque (Nm)")

plt.xlabel("Time (s)")
plt.tight_layout()
plt.show(block=True)