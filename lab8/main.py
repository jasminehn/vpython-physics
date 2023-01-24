GlowScript 3.2 VPython

#Constants
c=2.99792458e8
M_alpha=6.64465675e-27
M_other=3.82755500e-25
M_original=3.89402800e-25

#Energy Calculations
E_rest_original = M_original*c**2
Sum_rest_energy = M_alpha*c**2 + M_other*c**2

K1=(2)*(M_original-M_other-M_alpha)*c**2
K2 = M_other*(1+(M_other/M_alpha))
K3=(K1/K2)
v_2=K3**0.5

#v=((-M_original*c^2 - M_other*c^2 - M_alpha*c^2)/((0.5*M_other)+(0.5*(M_other^2/M_alpha))))^0.5
#v=((2/M_other)*((M_original*c^2-M_other*c^2-M_alpha*c^2)/(1+(M_other/M_alpha))))^0.5

v_alpha=(M_other*v_2)/(M_alpha)

print(v_2)
print(v_alpha)
