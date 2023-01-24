GlowScript 3.2 VPython

scene.width=600
scene.height=760

## Constants and data
g = 9.8
mball = 0.06
L0 = 0.26
ks = 1.80
deltat = 0.01
scalefactor = 0.5

## Objects
ceiling = box(pos=vector(0,0,0), size=vector(0.2, 0.01, 0.2)) 
ball = sphere(pos=vector(0.5,-0.3,0.5), radius=0.025, color=color.orange, make_trail=False)
spring = helix(pos=ceiling.pos, axis=ball.pos-ceiling.pos, color=color.cyan, thickness=0.003, coils=40, radius = 0.010)
P_arr = arrow(pos=vector(ball.pos, 0, 0), axis=vector(0,0.3, 0), color=color.red)
#F_arr = arrow(pos=vector(ball.pos, 0, 0), axis=vector(0.2,0,0), color=color.blue)
F_perp = arrow(pos=vector(ball.pos, 0, 0), axis=vector(0.2,0,0)*scalefactor, color=color.green)
F_para = arrow(pos=vector(ball.pos, 0, 0), axis=vector(0.2,0,0), color=color.green)

## Improve the display
scene.autoscale=False
scene.center = vector(0,-L0,0)

## initial values
pball = mball*vector(0,0,0)
Fgrav = mball*g*vector(0,-1,0)
scale1 = vector 

#graph
gd1 = gdisplay(y=0, xtitle='t', ytitle='y')
ygraph = gcurve(color=color.yellow)

scene.waitfor("click")

##calculation loop
t=0
while t<6:
  rate(100)
  Fspring=-ks*(spring.axis-vector(0,L0,0))*(spring.axis.mag)
  Fnet=Fgrav+Fspring
  pball=pball+Fnet*deltat
  ball.pos=ball.pos+(pball/mball)*deltat
  spring.axis = ball.pos - ceiling.pos
  
  P_arr.pos=ball.pos
  P_arr.axis=pball
  #F_arr.pos=ball.pos
  #F_arr.axis=Fnet
  
  Fpara = -pball
  Fperp = Fnet - Fpara
  
  F_perp.pos=ball.pos
  F_perp.axis=Fperp
  F_para.pos=ball.pos
  F_para.axis=Fpara
  
  t=t+deltat
  ygraph.plot(pos=(t,ball.pos.y))
  
