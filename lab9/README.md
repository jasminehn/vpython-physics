This program is a visualization of the motion of the spacecraft under the influence of the gravitational fields of the Earth and Moon, and also showing how the kinetic, potential and total energy of the spacecraft changes over time.

The program starts by defining some constants such as the gravitational constant 'G', the mass of the Earth 'mEarth', the mass of the spacecraft 'mCraft', and the mass of the Moon 'mMoon', and the time step 'deltat' and scale factors for the arrows 'scalefactor' and 'scalefactor2'.

Then it creates the 3D spheres and arrows representing the Earth, Moon, and spacecraft and sets their initial positions and velocities. It also creates two graphs, one for energy vs time, and one for energy vs separation.

The program then enters a while loop that continues until a certain time has passed. Inside the loop, it calculates the gravitational force of the Earth and Moon on the spacecraft, updates the momentum and position of the spacecraft using these forces, and updates the position and axis of the momentum and force arrows.
It also plots the kinetic, potential and total energy of the spacecraft on the graphs. It also checks if the distance between the spacecraft and the Earth is less than the radius of the Earth and breaks the loop if that's the case.

![image](https://user-images.githubusercontent.com/88569965/214215196-8932ec46-a5bc-4838-a69c-17a7374208b1.png)

![image](https://user-images.githubusercontent.com/88569965/214215169-e7f84594-6c74-4633-9a2b-9999a53ed80e.png)
