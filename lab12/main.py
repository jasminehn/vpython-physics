GlowScript 3.2 VPython

scene.width=600
scene.height=760

## Constants
g = 9.8
mball = 0.06
L0 = 0.26
ks = 1.8
deltat = 0.01
scalefactor = 0.5
c = 0.3
b = 0#.3

## Objects
ceiling = box(pos=vector(0,0,0), size=vector(0.2, 0.01, 0.2)) 
ball = sphere(pos=vector(0,-0.1,0), radius=0.025, color=color.orange, make_trail=False)
spring = helix(pos=ceiling.pos, axis=ball.pos-ceiling.pos, color=color.cyan, thickness=0.003, coils=40, radius = 0.010)
P_arr = arrow(pos=vector(ball.pos, 0, 0), axis=vector(0,0.3, 0), color=color.red)
F_perp = arrow(pos=vector(ball.pos, 0, 0), axis=vector(0.2,0,0)*scalefactor, color=color.green)
F_para = arrow(pos=vector(ball.pos, 0, 0), axis=vector(0.2,0,0), color=color.green)

## Improve the display
scene.autoscale=False
scene.center = vector(0,-L0,0)

## Initial values
pball = mball*vector(0,0,0)
Fgrav = mball*g*vector(0,-1,0)

## Energy vs. time graph
gd1 = gdisplay(y=0, xtitle='t', ytitle='y')
Kgraph = gcurve(color=color.green, dot=True, label='Kinetic')
Ugraph = gcurve(color=color.blue, dot=True, label='Potential')
KUgraph = gcurve(color=color.red, dot=True, label='Total')

scene.waitfor("click")

## Calculation loop
t=0
while t<20:
  rate(100)
  
  #calculate force/momentum without air drag initially
  Fspring = -ks*(spring.axis-vector(0,L0,0))*(spring.axis.mag)
  Fnet = Fgrav+Fspring
  pball = pball+Fnet*deltat
  
  #velocity of the ball (cannot be calculated before momentum)
  vball = pball/mball
  vhat = vball/vball.mag
  
  #update force/momentum with air drag (which includes velocity)
  Fdrag = (-c)*(mag(vball)**2)*vhat
  Fvisc = (-b)*mag(vball)*vhat
  Fnet = Fgrav+Fspring+Fdrag+Fvisc
  pball = pball+Fnet*deltat 
  
  #update ball and spring positions
  ball.pos = ball.pos+(pball/mball)*deltat
  spring.axis = ball.pos-ceiling.pos
  
  #add arrow representing ball's momentum
  P_arr.pos = ball.pos
  P_arr.axis = pball
  
  #calculate the parallel and perpendicular forces on the ball
  Fpara = -pball
  Fperp = Fnet-Fpara
  
  #add arrows representing the parallel and perpendicular forces
  F_perp.pos = ball.pos
  F_perp.axis = Fperp
  F_para.pos = ball.pos
  F_para.axis = Fpara
  
  #calculate potential, kinetic, and total energy
  U = -0.5*ks*(ball.pos.mag**2)+0.20
  K = 0.5*mball*((vball.mag)**2)
  KplusU = K+U
  
  t=t+deltat
  Ugraph.plot(pos=(t,U))
  Kgraph.plot(pos=(t,K))
  KUgraph.plot(pos=(t,KplusU))
  
