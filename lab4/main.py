GlowScript 3.2 VPython

G=6.67e-11
x=-13e7
dx=6.5e7
Mplanet=6e24
Mspacecraft=1.5e4
v1=vector(0,-2e7, 0)
v2=vector(-13e7, 4.5e7, 0)
rhat=(v2-v1)/(v2-v1).mag
scalefactor=50000;
Earth=sphere(pos=vector(0,-2e7, 0), radius=6.4e6, color=color.blue)
Spacecraft=sphere(pos=vector(-13e7, 4.5e7, 0), radius=3e6, color=color.red)
force=rhat*(-G*((Mplanet*Mspacecraft)/((v2-v1).mag2)))
print(force)
print(Spacecraft.pos - Earth.pos)
arrow(pos=vector(-13e7, 4.5e7, 0), axis=force*scalefactor, color=color.green)
while x<14e7:
  v3=vector(x,4.5e7,0)
  rhat2=(v3-v1)/(v3-v1).mag
  ball=sphere(pos=vector(x,4.5e7,0), color=color.yellow, radius=3e6)
  force2=rhat2*(-G*((Mplanet*Mspacecraft)/((v3-v1).mag2)))
  arrow(pos=vector(x,4.5e7,0), axis=force2*scalefactor, color=color.green, shaftwidth = 3.2e6)
  arrow(pos=vector(0,-2e7,0), axis=-force2*scalefactor, color=color.red, shaftwidth = 3.2e6)
  x=x+dx
  print(force2)
  
