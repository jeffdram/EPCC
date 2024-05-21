import math
import cmath

V=cmath.rect(100*math.sqrt(2),0)
w=100
R=10
L=100*10**-3
C=1000*10**-6
Xc=1/(w*C)
Xl=w*L
Z1=-Xc*1j
Z2=R+Xl*1j
Z=Z1*Z2/(Z1+Z2)
I=V/Z
print("módulo = ", abs(I))
print("fase = ", cmath.phase(I)*180/math.pi)



