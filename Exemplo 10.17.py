import math
import cmath


"""

Determinar os ajustes do relé de proteção geral de uma indústria em cuja subestação estão instalados dois transformadores a seco, com capacidade nominal de 750 kVA, cada unidade,
sendo que apenas um transformador está ligado. 

O segundo transformador somente será utilizado quando ocorrer a expansão do empreendimento. A impedância do transformador vale 6 %. 

A proteção geral da subestação é realizada por um disjuntor SF6 de 630 A da GE, associado a um relé digital Pextron URPE 7104, 
que recebe informações de corrente por um TC 10B200, com relação de transformação ajustada em 200-5 A.

O ponto de conexão da SE Indústria está distante da SE Concessionária, aproximadamente 15,81 km, assim distribuídos e em conformidade com a Figura 10.75. 

A ordem de ajuste da SE Concessionária está mostrada na Tabela 10.17.

Alimentador principal: 12,65 km em cabo de alumínio 266,8 MCM.
Ramal: 1,468 km em cabo de alumínio 1/0 AWG.
Sub-ramal: 1,699 km em cabo de cobre 16 mm2.
Ramal de entrada: 28 m em cabo isolado de 35 mm2 de cobre.

"""
# ----------------------------- Cálculo da tensão no circuito dos TCs ligados ao relé Pextron URPE 7104 ---------------------------------------- #

"""De acordo com o projeto, o relé está localizado a uma distância de 2,0 m dos transformadores de corrente e é alimentado por um circuito em cabo 2x1,5 mm2. 

As principais características técnicas dessa ligação são: """
Vn = 13800
Vnb = 380
S_Trafo = 750e3 #Transformador 750 kva
I_Trafo = S_Trafo/(Vn*math.sqrt(3)) # corrente nominal do trafo
Z_cabo_rele = 14.81 #Impedância de um cabo de 1,5 mm2:  Ω/km (Tabela 3.22)
Z_rele = 0.070 #Impedância do relé: Ω (Tabela 10.19)
In_rele = 5 # Corrente nominal do relé:  A
L_rele_TC = 2 # Distância entre o relé e os TCs: L = 2 m
Istc = 5 #Transformador de corrente para proteção: 200/400/600/800-5 A
RTC = 40 #Relação de transformação: 200-5 A = 40
FTC = 20 #Fator de sobrecorrente do TC: 20
Z_n_Trafo_perc = 0.06 # impedância nominal do transformador de 750 kVA
E_TC = RTC*Istc*(L_rele_TC*Z_cabo_rele/1000 + Z_rele) #A tensão nos terminais dos TCs vale:


# ----------------------------- Cálculo das impedâncias --------------------------------------- #

S_base = 100e6

# Ponto A
R_1_A = 0.0138 # em pu entrada
X_1_A = 0.4439 # em pu entrada
Z_1_A = R_1_A + X_1_A*1j
R_0_A = 0 # em pu entrada
X_0_A = 0.3453 # em pu entrada
Z_0_A = R_0_A + X_0_A*1j

# impedância do cabo 266,8MCM
L_cabo_266_8MCM = 12.65 # comprimento em km
R_cabo_1_266_8MCM = 0.2391 # Resistência de sequência positiva do cabo 266,8MCM ohms por km
X_cabo_1_266_8MCM = 0.3788 # Reatância de sequência positiva do cabo 266,8MCM ohms por km
Z_cabo_1_266_8MCM = (R_cabo_1_266_8MCM + X_cabo_1_266_8MCM*1j)*(S_base/Vn**2) # impedância do cabo 2666,8MCM em pu
R_cabo_0_266_8MCM = 0.4169 # Resistência de sequência zero do cabo 266,8MCM ohms por km
X_cabo_0_266_8MCM = 1.5559 # Reatância de sequência zero do cabo 266,8MCM ohms por km
Z_cabo_0_266_8MCM = (R_cabo_0_266_8MCM + X_cabo_0_266_8MCM*1j)*(S_base/Vn**2) # impedância do cabo 2666,8MCM em pu

# Ponto B

Z_1_B = Z_1_A + Z_cabo_1_266_8MCM*L_cabo_266_8MCM
Z_0_B = Z_0_A + Z_cabo_0_266_8MCM*L_cabo_266_8MCM

# impedância do cabo 1/0 AWG (CAA)
L_cabo_1barra0AWG = 1.468 # comprimento em km
R_cabo_1_1barra0AWG = 0.6955 # Resistência de sequência positiva do cabo 1/0AWG ohms por km
X_cabo_1_1barra0AWG = 0.4984 # Reatância de sequência positiva do cabo 1/0AWG ohms por km
Z_cabo_1_1barra0AWG = (R_cabo_1_1barra0AWG + X_cabo_1_1barra0AWG*1j)*(S_base/Vn**2) # impedância do cabo 1/0AWG em pu
R_cabo_0_1barra0AWG = 0.8733 # Resistência de sequência zero do cabo 1/0AWG ohms por km
X_cabo_0_1barra0AWG = 1.0219 # Reatância de sequência zero do cabo 1/0AWG ohms por km
Z_cabo_0_1barra0AWG = (R_cabo_0_1barra0AWG + X_cabo_0_1barra0AWG*1j)*(S_base/Vn**2) # impedância do cabo 1/0AWG em pu

# Ponto C

Z_1_C = Z_1_B + Z_cabo_1_1barra0AWG*L_cabo_1barra0AWG
Z_0_C = Z_0_B + Z_cabo_0_1barra0AWG*L_cabo_1barra0AWG

# impedância do cabo 16mm AWG
L_cabo_16mmAWG = 1.699 # comprimento em km
R_cabo_1_16mmAWG = 1.3080 # Resistência de sequência positiva do cabo 16mmAWG ohms por km
X_cabo_1_16mmAWG = 0.4802 # Reatância de sequência positiva do cabo 16mmAWG ohms por km
Z_cabo_1_16mmAWG = (R_cabo_1_16mmAWG + X_cabo_1_16mmAWG*1j)*(S_base/Vn**2) # impedância do cabo 16mmAWG em pu
R_cabo_0_16mmAWG = 1.4858 # Resistência de sequência zero do cabo 16mmAWG ohms por km
X_cabo_0_16mmAWG = 2.0045 # Reatância de sequência zero do cabo 16mmAWG ohms por km
Z_cabo_0_16mmAWG = (R_cabo_0_16mmAWG + X_cabo_0_16mmAWG*1j)*(S_base/Vn**2) # impedância do cabo 16mmAWG em pu


# Ponto D

Z_1_D = Z_1_C + Z_cabo_1_16mmAWG*L_cabo_16mmAWG
Z_0_D = Z_0_C + Z_cabo_0_16mmAWG*L_cabo_16mmAWG

# impedância do cabo 35mm AWG
L_cabo_35mmAWG = 0.26 # comprimento em km
R_cabo_1_35mmAWG = 0.862 # Resistência de sequência positiva do cabo 35mmAWG ohms por km
X_cabo_1_35mmAWG = 0.3567 # Reatância de sequência positiva do cabo 35mmAWG ohms por km
Z_cabo_1_35mmAWG = (R_cabo_1_35mmAWG + X_cabo_1_35mmAWG*1j)*(S_base/Vn**2) # impedância do cabo 35mmAWG em pu
R_cabo_0_35mmAWG = 1.3522 # Resistência de sequência zero do cabo 35mmAWG ohms por km
X_cabo_0_35mmAWG = 1.8222 # Reatância de sequência zero do cabo 35mmAWG ohms por km
Z_cabo_0_35mmAWG = (R_cabo_0_35mmAWG + X_cabo_0_35mmAWG*1j)*(S_base/Vn**2) # impedância do cabo 35mmAWG em pu

# Ponto E

Z_1_E = Z_1_D + Z_cabo_1_35mmAWG*L_cabo_35mmAWG
Z_0_E = Z_0_D + Z_cabo_0_35mmAWG*L_cabo_35mmAWG

# impedância do cabo 35mm 
L_cabo_35mm = 0.028 # comprimento em km
R_cabo_1_35mm = 1.0912 # Resistência de sequência positiva do cabo 35mm ohms por km
X_cabo_1_35mm = 0.1692 # Reatância de sequência positiva do cabo 35mm ohms por km
Z_cabo_1_35mm = (R_cabo_1_35mm + X_cabo_1_35mm*1j)*(S_base/Vn**2) # impedância do cabo 35mmAem pu
R_cabo_0_35mm = 2.5460 # Resistência de sequência zero do cabo 35mm ohms por km
X_cabo_0_35mm = 2.864 # Reatância de sequência zero do cabo 35m ohms por km
Z_cabo_0_35mm = (R_cabo_0_35mm + X_cabo_0_35mm*1j)*(S_base/Vn**2) # impedância do cabo 35mm em pu

# Ponto F

Z_1_F = Z_1_E + Z_cabo_1_35mm*L_cabo_35mm
Z_0_F = Z_0_E + Z_cabo_0_35mm*L_cabo_35mm



# Impedância do Trafo  em pu 
Z_Trafo_pu = Z_n_Trafo_perc*S_base/S_Trafo

#Cálculo da impedância de contato com a terra
#Será considerado o valor indicado pela concessionária, que é 100ohms
Z_terra = 100
Z_c_pu = Z_terra*S_base/Vn**2 #pu
# Impedância a considerar no cálculo da corrente minima, ainda não sei qual é
Z_pu_qual = 10

# ----------------------------- Cálculo das correntes de curto --------------------------------------- #

# Curto-circuito trifásico no ponto de conexão
Icc3f_ent = 1/Z_1_E*(S_base/Vn)
# Corrente de curto-circuito fase-terra máxima ponto de conexão
Icc1ft_max_ent = (3/(2*Z_1_E + Z_0_E))*(S_base/Vn)*1/math.sqrt(3)
# Corrente de curto-circuito fase-terra mínima ponto de conexão
Icc1ft_min_ent = (3/(2*Z_1_E + Z_0_E+Z_Trafo_pu+Z_pu_qual + 3*Z_c_pu))*(S_base/Vn)*1/math.sqrt(3)
# Corrente de curto-circuito no barramento da SE Indústria
Icc3f_tf = 1/Z_1_F*(S_base/Vn)*1/math.sqrt(3)
# Corrente de curto-circuito fase-terra máxima no barramento da SE Indústria
Icc1ft_max_tf = (3/(2*Z_1_F + Z_0_F))*(S_base/Vn)*1/math.sqrt(3)
# Corrente de curto-circuito fase-terra mínima no barramento da SE Indústria
Icc1ft_min_tf = (3/(2*Z_1_F + Z_0_F+Z_Trafo_pu+Z_pu_qual + 3*Z_c_pu))*(S_base/Vn)*1/math.sqrt(3)
# Corrente de curto-circuito no barramento da SE Indústria lado de baixa
Icc3f_tf_b = 1/(Z_1_F+Z_Trafo_pu)*(S_base/Vnb)*1/math.sqrt(3)
# Corrente de curto-circuito fase-terra lado de baixa
Icc1ft_tf_b = (3/(2*Z_1_F + Z_Trafo_pu))*(S_base/Vnb)*1/math.sqrt(3)

# ----------------------------- Cálculo da corrente de magnetização do transformador de força --------------------------------------- #

#Proteção do alimentador 01I2 da SE Concessionária - SEL351-6D4E642X2

# Proteção de sobrecorrente de fase (50/51)
Ipickup = 500 # pickup A
tms_c= 0.26 # curva_ajuste da concessionária
tipo_curva_ajuste = "muito inversa"
Ipickup_N = 26 # pickup A
tms_c_N= 0.64 # curva_ajuste da concessionária

I_mg_Trafo = 8*I_Trafo # Corrente de magnetização do trafo
t_mg_Trafo = 0.1 # tempo de  magnetização do trafo
I_Trafo_ANSI = I_mg_Trafo/Z_n_Trafo_perc
t_ANSI = 3.5 # valor atribuído para o tempo do ponto ANSI

# Determinação do tempo de resposta do relé temporizado de fase (51) da SE
t_rc = 13.5/((abs(Icc3f_tf)/Ipickup)-1)*tms_c # tempo do rele da concessionaria

# Determinação da corrente de atuação da unidade temporizada de fase do relé da SE Indústria (51)
Iat = 1.2*I_Trafo # Corrente temporizada (51)
Ia51_F = Iat/RTC # Corrente de ajuste temporizada (51)
t_ri = t_rc-5.1 # Determinação do tempoe curva de atuaçãoda unidade temporizada de fase do relé da SE Indústria(51)
tms = t_ri*((abs(Icc3f_tf)/Ipickup)-1)/13.5 #tempo da curva de ajuste do cliente

# Determinação da corrente de atuação da unidade tempo definido de fase do relé cliente
Ia50_F = 2*I_mg_Trafo/RTC
t_aj = 0.1 # tempo de ajuste definido

# Determinação do tempo de resposta do relé temporizado de fase (51N) da SE
t_rc_N = 13.5/((abs(Icc1ft_min_tf)/Ipickup_N)-1)*tms_c_N # tempo do rele da concessionaria

# Determinação da corrente de atuação da unidade temporizada de fase do relé da SE Indústria (51N)
I_des = Iat*0.2  # Corrente temporizada (51N)
Ia51_N = I_des/RTC # Corrente de ajuste temporizada (51N)
t_ri_N = t_rc_N-4.4 # Determinação do tempoe curva de atuaçãoda unidade temporizada de fase do relé da SE Indústria(51N)
tms_N = t_ri_N*((abs(Icc1ft_min_tf)/Ipickup_N)-1)/13.5 #tempo da curva de ajuste do cliente

# Determinação da corrente de atuação da unidade tempo definido de fase do relé cliente
Ia50_N = 0.1*Istc
t_aj_N = 0 # tempo de ajuste definido


