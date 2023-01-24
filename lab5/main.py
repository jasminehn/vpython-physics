GlowScript 3.2 VPython

#Constants
G = 6.7e-11
mEarth = 6e24
mcraft = 15e3
deltat = 60

#Objects
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
craft = sphere(pos=vector(-10*Earth.radius, 0, 0), radius=1e6, color=color.yellow, make_trail=True)

#Definitions and initial values
vcraft = vector(0,3550,0) 
pcraft = mcraft*vcraft

r2 = craft.pos - Earth.pos 
force=(G*((mEarth*mcraft)/((r2).mag2)))

print(pcraft)
sf = 0.5

parr = arrow(pos=vector(-10*Earth.radius, 0, 0), axis=vector(0, force*sf, 0), color=color.green)
farr = arrow(pos=vector(-10*Earth.radius, 0, 0), axis=vector(0,force*sf, 0), color=color.red)

#iterations
t=0
scene.autoscale = False #turn off automatic camera zoom
while t<10*365*24*60*60:
  rate(1000)
  sf2 = 10
  r = craft.pos - Earth.pos 
  rhat = r / r.mag
  Fmag = G * mEarth * mcraft / r.mag2 
  F_on1 = Fmag * (-rhat)
  pcraft = pcraft + F_on1 * deltat 
  craft.pos = craft.pos + (pcraft/mcraft) * deltat 
  parr.pos = craft.pos
  parr.axis = pcraft * sf
  force2=vector(Fmag, Fmag, 0)
  farr.pos = craft.pos
  farr.axis = F_on1 * sf2
  t = t+deltat
  if mag(r) < Earth.radius:
    break #exit the loop
