This Python script suite integrates three distinct physical simulations—random walk diffusion, polarization state evolution via Jones calculus, and 2D ray tracing through thin lenses—each accompanied by visualizations and animations to enhance conceptual understanding.
# 1. 🌀 Random Walk Diffusion Simulation
#  • 	Objective: Simulate and visualize the stochastic motion of particles undergoing a 2D random walk.
# • 	Methodology:
• 	Initializes 500 particles at the origin in 2D space.
• 	Each particle performs a symmetric random walk over 500 time steps.
• 	Tracks particle positions over time and computes the Mean Squared Displacement (MSD).
• 	Compares simulated MSD with theoretical predictions using the diffusion relation:
• 	Visualization:
• 	Static plot of MSD vs. time with theoretical overlay.
• 	Animated GIF showing particle dispersion over time in 2D space.
# 2. 🔬 Polarization State Tracking via Jones Calculus
# • 	Objective: Model the transformation of light polarization through optical components.
#  • 	Methodology:
• 	Constructs Jones vectors for linear polarization and matrices for a quarter-wave plate (QWP), half-wave plate (HWP), and polarizer.
• 	Applies sequential transformations to an input light beam polarized at 45°.
• 	Computes the output polarization state after passing through QWP → HWP → Polarizer.
• 	Visualization:
• 	Vector plot comparing input and output electric field components in the polarization plane.
# 3. 🔭 2D Ray Tracing Through Thin Lenses
• 	Objective: Simulate light ray propagation through a system of thin lenses.
• 	Methodology:
• 	Defines two lenses with specified positions and focal lengths.
• 	Initializes multiple rays at varying vertical positions.
• 	Applies paraxial ray tracing principles to compute ray deflections at lens interfaces.
• 	Visualization:
• 	Static plot showing ray trajectories and lens positions.
• 	Animated GIF illustrating dynamic ray propagation across the optical system.
🗂 Output Summary
• 	All plots and animations are saved in organized directories:
• 	: MSD plot and random walk animation.
• 	: Polarization vector plot.
• 	: Ray tracing plot and propagation animation.

This codebase serves as an educational toolkit for visualizing key physical phenomena in statistical mechanics and optics, combining numerical simulation with intuitive graphical outputs. Let me know if you'd like this abstract formatted for a report or presentation slide.

![](figures_diffusion/random_walk_2d.gif)


![](figures_diffusion/msd_vs_time.png)



![](figures_ray_tracing/ray_propagation.gif)


A pair of Python scripts to explore basic physics simulations:

- **random_walk_diffusion.py**: Simulates a 1D/2D random walk of multiple particles, computes mean squared displacement (MSD), compares to theoretical diffusion, and generates plots and an animation.  
- **optics_simulation_full.py**: Tracks polarization states via Jones calculus, performs 2D ray tracing through thin lenses, and produces static plots plus an animation of ray propagation.


## Features

- Monte Carlo simulation of particle diffusion with MSD calculation  
- Comparison of simulated MSD against theoretical predictions  
- Animated 2D random walk saved as a GIF  
- Polarization manipulation using Jones matrices (linear, quarter-wave, half-wave, polarizer)  
- 2D ray tracing through configurable thin lenses  
- Static and animated visualizations for optics processes  


## Dependencies

- Python 3.6 or higher  
- NumPy  
- Matplotlib  
- Pillow (for GIF export)  



## Installation


3. Install required packages  

  pip install numpy matplotlib pillow

## Usage

All figures and animations are saved under dedicated folders. Run each script independently:

 **Diffusion simulation**  

  python random_walk_diffusion.py
 

- **Optics simulation**  

  python optics_simulation_full.py



 **Parameters**  
  - `N_particles`: Number of particles  
  - `N_steps`: Number of time steps  
  - `dim`: Dimensionality (1 or 2)  
  - `step_size`: Size of each random step  

- **Workflow**  
  1. Initialize all particles at the origin  
  2. Perform random ±step moves each axis  
  3. Record position history and compute MSD  
  4. Plot simulated vs theoretical MSD  
  5. Animate 2D trajectories and save as GIF  

- **Output**  
  - `figures_diffusion/msd_vs_time.png`  
  - `figures_diffusion/random_walk_2d.gif`  

### optics_simulation_full.py

- **Polarization Tracking**  
  - Defines Jones vectors for horizontal, vertical, linear polarization  
  - Builds Jones matrices for quarter-wave, half-wave plates, and a polarizer  
  - Applies sequence to an input vector and plots input vs output  

- **2D Ray Tracing**  
  - Configurable thin lenses with position and focal length  
  - Traces multiple rays through free space and lens refractions  
  - Saves static plot of ray paths  

- **Animation**  
  - Builds a frame-by-frame GIF showing ray propagation  


## Contributing

Contributions are welcome. Feel free to:

- Open issues for bug reports or feature requests  
- Submit pull requests with enhancements or fixes  
- Suggest improvements to documentation or examples  


## License

This project is released under the MIT License.  


![](figures_polarization/polarization_jones.png)
