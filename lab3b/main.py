GlowScript 3.2 VPython

track=box(pos=vector(0, -0.025, 0), size=vector(2.0, 0.05, 0.10), color=color.white)
cart=box(pos=vector(1,0.03,0), size=vector(0.1,0.04,0.06), color=color.yellow)
mcart=0.80 # in kg
pcart=mcart*vector(0.5,0,0) # in kg m/s
print ("cart momentum =", pcart)
deltat = 0.01 # in s
t = 0 # in s, initial time
while t < 14: # this is the start of the loop
  #print ('the time is now', t) #indented code is part of the loop
  cart.pos = cart.pos - (pcart/mcart)*deltat
  t = t + deltat # this is the last line of the loop, updates time t
  F_air=vector(0.055,0,0)
  Fnet= -F_air
  pcart = pcart + Fnet*deltat
  print ('position of cart: ', cart.pos)
  rate(350)
print ('after the loop') # unindent, executes after loop finishes
