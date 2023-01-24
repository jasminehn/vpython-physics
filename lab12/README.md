This program is simulating the motion of the ball connected to the spring under the influence of gravity, drag and viscosity forces, and also showing how the momentum, parallel force, and perpendicular force of the ball changes over time, also it is showing how kinetic, potential and total energy of the ball changes over time.

The program starts by setting the width and height of the scene and defining some constants such as the acceleration due to gravity 'g', the mass of the ball 'mball', the rest length of the spring 'L0', the spring constant 'ks', the time step 'deltat', and a scale factor for the arrows 'scalefactor', the drag coefficient 'c', and the viscosity coefficient 'b'.

Then it creates the 3D box for the ceiling, sphere for the ball, and helix for the spring and sets their initial positions. It also creates the arrows to represent the momentum, parallel force, and perpendicular force.

The program then enters a while loop that continues until a certain time has passed. Inside the loop, it first calculates the gravitational force and spring force acting on the ball, then it calculates the drag and viscosity force, then it updates the momentum and position of the ball using these forces, and updates the position and axis of the arrows representing the momentum, parallel force, and perpendicular force.

Lastly, it plots the kinetic energy, potential energy and total energy of the ball over time on a graph.

![image](https://user-images.githubusercontent.com/88569965/214216905-5b40d860-3583-48e3-bade-3c3f526ba62a.png)
