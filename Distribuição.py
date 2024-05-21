import math
import cmath


"""

O diagrama unifilar de um sistema de distribuição primário (13,8kV), aéreo, trifásico a três fios e aterrado na S/E. 

Estão representados os equipamentos de proteção comumente utilizados: Disjuntor (52) ; Relés (51), que comandam o disjuntor; 
Transformadores de Corrente (TC), que alimentam os relés ; Religador (R); Seccionalizador (S), que opera em conjunto com o religador e 
Chave-Fusível (CF), cujo dispositivo sensor é o Elo-Fusível. Além destes equipamentos, 
estão representados os Transformadores de Força (TF) e de Distribuição (TD) , localizados na S/E e nos ramais, 
respectivamente. 

"""

# potência de curto trifásico na barra de 69kV, na S/E: SCC,3 φ = √3 V ICC, 3 φ = 120MVA
# para um espaçamento equivalente dos condutores de 1,355m, as impedâncias de seqüências são:

V_b_alta = 69e3 # tensão da barra 
V_b_media = 13.8e3 # tensão da distribuição
S_tf = 15e6 # potência do trafo

Scc3f_b_alta = 120e6 # potência de curto trifásica na barra alta
Icc3f_b_alta = Scc3f_b_alta/(math.sqrt(3)*V_b_alta) # corrente de curto trifásica na barra alta

Z1_tf_perc = 0.08 #impedância positiva percentual do trafo
Z0_tf_perc = Z1_tf_perc #impedância zero percentual do trafo

Z1_c_2b0 = 0.4387 + 0.4567j  # Cabo 2/0 CAA Ω/km
Z2_c_2b0 = Z1_c_2b0 # Cabo 2/0 CAA Ω/km
Z0_c_2b0 = 0.6163 + 1.9195j # Cabo 2/0 CAA Ω/km
Z1_c_1b0 = 0.5499 + 0.4501j
Z2_c_1b0 = Z1_c_1b0 # Cabo 2/0 CAA Ω/km
Z0_c_1b0 = 0.7275 + 1.9069j # Cabo 2/0 CAA Ω/km

L_A_B = 8 # trecho A-B km
L_B_C = 6 # trecho B-C km
L_B_D = 3 # trecho B-D km

# Para os curtos envolvendo a terra fora da S/E, considerar resistência de terra igual a 33,3Ω : 3RT =100Ω (valor recomendado pelo CCON)
RT=33.3 #resistência de terra fora da SE
# No caso de curtos envolvendo a terra dentro da S/E , considerá-los FRANCOS, isto é, fazer a resistência de terra igual a ZERO : RF = 0
RF=0 #resistência de falta dentro da SE

# ----------------------------------------- Resolução ---------------------------------------- #

# Impedância de sequência positiva equivalente do sistema, vista da barra de AT da S/E
Z1_S = 1j*(V_b_media**2)/Scc3f_b_alta
# Impedâncias de sequências positiva e negativa do transformador:
X1_tf = Z1_tf_perc*(V_b_media**2)/S_tf
Z1_tf = X1_tf*1j
Z0_tf = Z1_tf

# Impedâncias por trecho
Z1_c_AB = L_A_B*Z1_c_2b0 # trecho AB
Z0_c_AB = L_A_B*Z0_c_2b0 # trecho AB
Z1_c_BC = L_B_C*Z1_c_2b0 # trecho BC
Z0_c_BC = L_B_C*Z0_c_2b0 # trecho BC
Z1_c_BD = L_B_D*Z1_c_1b0 # trecho BD
Z0_c_BD = L_B_D*Z0_c_1b0 # trecho BD

Z1_A = Z1_tf+Z1_S
Z2_A = Z1_A
Z0_A_1 = Z0_tf+RF
Z0_A_2 = Z0_tf+3*RT
Z1_B = Z1_A+Z1_c_AB
Z2_B = Z1_B
Z0_B = Z0_A_2+Z0_c_AB
Z1_C = Z1_B+Z1_c_BC
Z2_C = Z1_C
Z0_C = Z0_B+Z0_c_BC
Z1_D = Z1_B+Z1_c_BD
Z2_D = Z1_D
Z0_D = Z0_B+Z0_c_BD


# Determinação dos curtos na Barra A (S/E)
Icc3f_A = (V_b_media/math.sqrt(3))/(Z1_A) # corrente de curto trifásica na barra alta
Icc2f_A = Icc3f_A*(math.sqrt(3)/2) # Curto Bifásico (diagramas se seqüências pos. e neg.)
Icc2fT_A = -3*Icc3f_A*(Z1_A)/(Z1_A+2*Z0_tf) # Curto Bifásico terra (diagramas se seqüências pos. e neg.)
Icc1fT_A = 3*Icc3f_A*(Z1_A)/(2*Z1_A+Z0_tf) #  Curto Fase-Terra (diagramas de seqüências. pos., neg. e zero)

# Determinação dos curtos na Barra B
Icc3f_B = (V_b_media/math.sqrt(3))/(Z1_B) # corrente de curto trifásica na barra alta
Icc2f_B = Icc3f_B*(math.sqrt(3)/2) # Curto Bifásico (diagramas se seqüências pos. e neg.)
Icc2fT_B = -3*Icc3f_B*(Z1_B)/(Z1_B+2*Z0_B) # Curto Bifásico terra (diagramas se seqüências pos. e neg.)
Icc1fT_B = 3*Icc3f_B*(Z1_B)/(2*Z1_B+Z0_B) #  Curto Fase-Terra (diagramas de seqüências. pos., neg. e zero)

# Determinação dos curtos na Barra C
Icc3f_C = (V_b_media/math.sqrt(3))/(Z1_C) # corrente de curto trifásica na barra alta
Icc2f_C = Icc3f_C*(math.sqrt(3)/2) # Curto Bifásico (diagramas se seqüências pos. e neg.)
Icc2fT_C = -3*Icc3f_C*(Z1_C)/(Z1_C+2*Z0_C) # Curto Bifásico terra (diagramas se seqüências pos. e neg.)
Icc1fT_C = 3*Icc3f_C*(Z1_C)/(2*Z1_C+Z0_C) #  Curto Fase-Terra (diagramas de seqüências. pos., neg. e zero)

# Determinação dos curtos na Barra D
Icc3f_D = (V_b_media/math.sqrt(3))/(Z1_D) # corrente de curto trifásica na barra alta
Icc2f_D = Icc3f_D*(math.sqrt(3)/2) # Curto Bifásico (diagramas se seqüências pos. e neg.)
Icc2fT_D = -3*Icc3f_D*(Z1_D)/(Z1_D+2*Z0_D) # Curto Bifásico terra (diagramas se seqüências pos. e neg.)
Icc1fT_D = 3*Icc3f_D*(Z1_D)/(2*Z1_D+Z0_D) #  Curto Fase-Terra (diagramas de seqüências. pos., neg. e zero)

print("Icc3f na Barra A = ",abs(Icc3f_A))
print("Icc2f na Barra A = ",abs(Icc2f_A))
print("Icc2fT na Barra A = ",abs(Icc2fT_A))
print("Icc1fT na Barra A = ",abs(Icc1fT_A))
print("Icc3f na Barra B = ",abs(Icc3f_B))
print("Icc2f na Barra B = ",abs(Icc2f_B))
print("Icc2fT na Barra B = ",abs(Icc2fT_B))
print("Icc1fT na Barra B = ",abs(Icc1fT_B))
print("Icc3f na Barra C = ",abs(Icc3f_C))
print("Icc2f na Barra C = ",abs(Icc2f_C))
print("Icc2fT na Barra C = ",abs(Icc2fT_C))
print("Icc1fT na Barra C = ",abs(Icc1fT_C))
print("Icc3f na Barra D = ",abs(Icc3f_D))
print("Icc2f na Barra D = ",abs(Icc2f_D))
print("Icc2fT na Barra D = ",abs(Icc2fT_D))
print("Icc1fT na Barra D = ",abs(Icc1fT_D))
