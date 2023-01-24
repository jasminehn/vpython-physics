This program is a simulation of a ball connected to a spring hanging from a ceiling. It is simulating the motion of the ball connected to the spring under the influence of gravity, and also showing how the momentum, total force, parallel force, and perpendicular force of the ball changes over time.

The program starts by setting the width and height of the scene and defining some constants such as the acceleration due to gravity 'g', the mass of the ball 'mball', the rest length of the spring 'L0', the spring constant 'ks', the time step 'deltat', and a scale factor for the arrows 'scalefactor'.

It creates the 3D box for the ceiling, sphere for the ball, and helix for the spring and sets their initial positions. It also creates the arrows to represent the momentum, total force, parallel force, and perpendicular force.

The program then enters a while loop that continues until a certain time has passed. Inside the loop, it calculates the gravitational force and spring force acting on the ball, updates the momentum and position of the ball using these forces, and updates the position and axis of the arrows representing the momentum, total force, parallel force, and perpendicular force.

Lastly, it plots the position of the ball over time on a graph.

![image](https://user-images.githubusercontent.com/88569965/214216128-eb0b3a19-6384-451f-ab80-3323b50a0dae.png)
