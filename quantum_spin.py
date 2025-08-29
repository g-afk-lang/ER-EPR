#Quantum spin of a photon after being split into two identical photons, from the which way experiment.
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# --- Parameters ---
r = 1.0  # Radius of the cylinder
h = 2.5  # Height of the cylinder
animation_frames = 100  # Number of frames for a smooth animation

# --- Set up the Figure and 3D Axis ---
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# --- Animation Update Function ---
# This function is called for each frame of the animation
def update(frame):
    # Clear the previous frame to draw the new one
    ax.clear()

    # Calculate the current angle of the cylinder's arc
    # It will grow from pi (180 degrees) to 2*pi (360 degrees)
    current_angle = np.pi + (np.pi * (frame / animation_frames))

    # Create the grid of points for the cylinder surface
    theta = np.linspace(0, current_angle, 50)  # Angle array
    z = np.linspace(0, h, 20)                  # Height array
    theta_grid, z_grid = np.meshgrid(theta, z)

    # Convert from cylindrical coordinates to Cartesian (x, y, z)
    x_grid = r * np.cos(theta_grid)
    y_grid = r * np.sin(theta_grid)

    # Plot the surface
    ax.plot_surface(x_grid, y_grid, z_grid, color='cyan', alpha=0.7, edgecolor='k', linewidth=0.2)

    # --- Set Plot Appearance (for every frame) ---
    ax.set_xlim([-r, r])
    ax.set_ylim([-r, r])
    ax.set_zlim([0, h])
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title(f'Transformation: Frame {frame}/{animation_frames}')
    ax.view_init(elev=20., azim=30 + frame) # Rotate the view for a dynamic effect

# --- Create and Run the Animation ---
# FuncAnimation calls the 'update' function for each frame
ani = FuncAnimation(fig, update, frames=animation_frames, interval=50)

# Display the plot
plt.show()
