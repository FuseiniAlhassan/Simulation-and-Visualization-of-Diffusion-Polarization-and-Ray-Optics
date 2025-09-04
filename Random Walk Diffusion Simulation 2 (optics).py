# optics_simulation_full.py
import os
import numpy as np
import matplotlib.pyplot as plt

# Create output directories
FIG_DIR_POL = "figures_polarization"
FIG_DIR_RAY = "figures_ray_tracing"
for d in [FIG_DIR_POL, FIG_DIR_RAY]:
    os.makedirs(d, exist_ok=True)

# Part 1: Polarization State Tracking

def jones_horizontal(): return np.array([[1],[0]])
def jones_vertical(): return np.array([[0],[1]])
def jones_linear(theta_deg):
    theta = np.radians(theta_deg)
    return np.array([[np.cos(theta)], [np.sin(theta)]])
def jones_quarter_waveplate(theta_deg):
    theta = np.radians(theta_deg)
    J = np.array([[np.cos(theta)**2 + 1j*np.sin(theta)**2, (1-1j)*np.sin(theta)*np.cos(theta)],
                  [(1-1j)*np.sin(theta)*np.cos(theta), np.sin(theta)**2 + 1j*np.cos(theta)**2]])
    return J
def jones_half_waveplate(theta_deg):
    theta = np.radians(theta_deg)
    return np.array([[np.cos(2*theta), np.sin(2*theta)],
                     [np.sin(2*theta), -np.cos(2*theta)]])
def jones_polarizer(theta_deg):
    theta = np.radians(theta_deg)
    return np.array([[np.cos(theta)**2, np.cos(theta)*np.sin(theta)],
                     [np.cos(theta)*np.sin(theta), np.sin(theta)**2]])

# Input light
E_in = jones_linear(45)
QWP = jones_quarter_waveplate(0)
HWP = jones_half_waveplate(22.5)
POL = jones_polarizer(0)
E_out = POL @ HWP @ QWP @ E_in

# Plot polarization
fig, ax = plt.subplots(figsize=(6,6))
ax.quiver(0,0,np.real(E_in[0,0]),np.real(E_in[1,0]),angles='xy',scale_units='xy',scale=1,color='blue',label='Input')
ax.quiver(0,0,np.real(E_out[0,0]),np.real(E_out[1,0]),angles='xy',scale_units='xy',scale=1,color='red',label='Output')
ax.set_xlim(-1,1); ax.set_ylim(-1,1)
ax.set_xlabel('Ex'); ax.set_ylabel('Ey')
ax.set_title('Polarization: Jones Calculus')
ax.grid(True); ax.legend()
plt.savefig(os.path.join(FIG_DIR_POL, "polarization_jones.png"), dpi=200)
plt.close(fig)
print("Saved polarization plot.")

# Part 2: 2D Ray Tracing Engine
# Lenses: position (x), focal length (f)
lenses = [{'x': 5.0, 'f': 2.0}, {'x': 10.0, 'f': 3.0}]
y0 = np.linspace(-2, 2, 11)
x_max = 15
x_plot = np.linspace(0, x_max, 500)
ray_paths = []

for y_start in y0:
    x_ray, y_ray = [0], [y_start]
    angle = 0.0
    x_curr, y_curr = 0, y_start
    for x_next in x_plot[1:]:
        dx = x_next - x_curr
        y_curr += dx*np.tan(angle)
        for lens in lenses:
            if x_curr < lens['x'] <= x_next:
                y_lens = y_curr
                angle = angle - y_lens / lens['f']
        x_curr = x_next
        x_ray.append(x_curr)
        y_ray.append(y_curr)
    ray_paths.append((x_ray, y_ray))

# Plot rays
fig, ax = plt.subplots(figsize=(10,5))
for x_ray, y_ray in ray_paths:
    ax.plot(x_ray, y_ray, 'b')
for lens in lenses:
    ax.axvline(lens['x'], color='r', linestyle='--', label='Lens')
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title('2D Ray Tracing through Thin Lenses')
ax.grid(True)
plt.savefig(os.path.join(FIG_DIR_RAY, "ray_tracing.png"), dpi=200)
plt.close(fig)
print("Saved ray tracing plot.")

# Optional: Animate ray propagation (simple) and save GIF

import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(10,5))
lines = [ax.plot([],[], 'b')[0] for _ in ray_paths]
for lens in lenses:
    ax.axvline(lens['x'], color='r', linestyle='--')

ax.set_xlim(0, x_max); ax.set_ylim(-3, 3)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title('Ray Propagation Animation')
ax.grid(True)

def init():
    for line in lines:
        line.set_data([],[])
    return lines

def animate(frame):
    for i, (x_ray, y_ray) in enumerate(ray_paths):
        lines[i].set_data(x_ray[:frame], y_ray[:frame])
    return lines

ani = animation.FuncAnimation(fig, animate, frames=len(x_plot), init_func=init,
                              blit=True, interval=30)
ani.save(os.path.join(FIG_DIR_RAY, "ray_propagation.gif"), writer='pillow', fps=25)
plt.close(fig)
print("Saved ray propagation animation GIF.")