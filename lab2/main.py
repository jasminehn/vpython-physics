Web VPython 3.2

scene=canvas()
scene.autoscale = False
X=sphere(pos=vector(-2.5,0,0), radius=1, color=color.green)
Y=sphere(pos=vector(0,2,0), radius=1, color=color.green)
Z=sphere(pos=vector(0,-2,0), radius=1, color=color.green)
arrow(pos=vector(-2.5,0,0), axis=Z.pos-X.pos, color=color.red)
arrow(pos=vector(0,2,0), axis=X.pos-Y.pos, color=color.red)
arrow(pos=vector(0,-2,0), axis=Y.pos-Z.pos, color=color.red)
print(X.pos)
