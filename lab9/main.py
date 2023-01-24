GlowScript 3.2 VPython

#Constants
G = 6.7e-11
mEarth = 6e24
mCraft = 30e3
mMoon = 7e22
deltat = 1000
scalefactor = .5
scalefactor2 = 20000

#Objects
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
Moon = sphere(pos=-vector(-4e8,0,0), radius = 1.75e6, color=color.white)
craft = sphere(pos=vector(-10*Earth.radius, 0, 0), radius=1e6, color=color.yellow, make_trail=True)
Parr = arrow(pos=vector(-10*Earth.radius, 0, 0), axis=vector(0, 30000000, 0)*scalefactor, color=color.red)
Marr = arrow(pos=vector(-10*Earth.radius, 0, 0), axis=vector(1472,0,0)*scalefactor2,color=color.blue)

#Definitions and initial values
vcraft = vector(0,3.2735e3,0)
pcraft = mCraft*vcraft

#print values
print(pcraft)

#iterations
t=0
scene.autoscale = False #turn off automatic camera zoom
scene.center = (Earth.pos + Moon.pos)/2

#Energy vs. time graph
gd1 = gdisplay(x=600, y=0, xtitle='t', ytitle='Energy')
Kgraph = gcurve(color=color.yellow, dot=True, label='Kinetic')
Ugraph = gcurve(color=color.red, dot=True, label='Potential')
KplusUgraph = gcurve(color=color.cyan, dot=True, label='Total')

#Energy vs. separation graph
gd2 = gdisplay(x=600, y=400, xtitle='r', ytitle='Energy')
Kgraph_r = gcurve(color=color.yellow, dot=True, label='Kinetic')
Ugraph_r = gcurve(color=color.red, dot=True, label='Potential')
KplusUgraph_r = gcurve(color=color.cyan, dot=True, label='Total')

while t<10*365*24*60*60:
  rate(10000)
  
  #gravitational force of the Earth
  r = craft.pos - Earth.pos 
  rhat = r / r.mag
  Fmag = G * mEarth * mCraft / r.mag2 
  F_on1 = Fmag * (-rhat)
  
  #gravitational force of the moon
  r2 = craft.pos - Moon.pos 
  rhat2 = r2 / r2.mag
  Fmag2 = G * mMoon * mCraft / r2.mag2 
  F2_on1 = Fmag2 * (-rhat2)
  
  pcraft = pcraft + (F_on1 * deltat) + (F2_on1 * deltat) 
  craft.pos = craft.pos + (pcraft/mCraft) * deltat 
  Parr.pos=craft.pos
  Parr.axis=pcraft*scalefactor
  Marr.pos=craft.pos
  Marr.axis=F_on1*scalefactor2
  t = t+deltat
  if mag(r) < Earth.radius:
    break #exit from loop
  
  vCraft = (pcraft/mCraft).mag
  
  K1 = 0.5*mCraft*(vCraft**2)
  #U1 = (mCraft*-9.8*(r.mag))*25 # m*-g*deltaY
  U1 = -K1
  Kgraph.plot(pos=(t,K1))
  Ugraph.plot(pos=(t,U1))
  KplusUgraph.plot(pos=(t,K1+U1))
  
  print (K1 , U1)
  
  K2 = 0.5*mCraft*(vCraft**2)
  #U2 = mCraft*-9.8*(craft.pos-Earth.pos).mag # m*-g*deltaY
  U2 = -K2
  Kgraph_r.plot(pos=(r.mag,K2))
  Ugraph_r.plot(pos=(r.mag,U2))
  KplusUgraph_r.plot(pos=(r.mag,K2+U2))
