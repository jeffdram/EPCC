import cmath

# --------- valores de base ----------- #

vb = 13800  # tensão de base
sb = 100e6  # potência de base
zb = vb**2 / sb  # impedância de base
ib = sb / (vb * cmath.sqrt(3))  # corrente de base

# --------- primeiras informações da concessionária ----------- #

# impedâncias
z1r = 3.21 + 4.17j  # impedância da rede
z0r = 4.73 + 16.7j  # impedância da malha de terra
rf = 40  # resistência de falta

# curto circuito
icc3f = 795  # corrente de curto circuito trifásica simétrica
icc3fa = 811  # corrente de curto circuito trifásica assimétrica
iccft = 450  # corrente de curto circuito monofásico para terra
iccfta = 482  # corrente de curto circuito monofásica para terra assimétrica
iccftm = 307  # corrente de curto circuito monofásica para terra mínima, onde se leva em consideração uma resistência de falta

# ajustes da proteção
pf = 120  # partida de fase
iff = 800  # instantânea de fase
dtf = 0.5  # dial time fase
# cf = IEC-NI  # curva de fase
pn = 15  # partida de neutro
insn = 150  # instantânea de neutro
# cn = IEC-NI  # curva de neutro
dtn = 0.2  # dial time de neutro

# --------- informações da subestação ----------- #

# cabo de entrada
cb = 35  # cabo bitola media tensão
z_un_cb = 0.67 + 0.147j  # (ohm/km) procurar valor na tabela do fabricante
lcb = 500  # comprimento do cabo
z1cbpu = z_un_cb * lcb / 1000  # impedância cabo em pu

# transformadores
tf1 = 500e3  # potência do trafo 1
ztf1 = 0.055  # impedância percentual do trafo 1
kinrush1 = 10  # fator k da corrente de magnetização do trafo 1
intf1 = tf1 / (vb * cmath.sqrt(3))  # corrente no trafo 1
tf2 = 750e3  # potência do trafo 2
ztf2 = 0.045  # impedância percentual do trafo 2
kinrush2 = 8  # fator k da corrente de magnetização do trafo 2
intf2 = tf2 / (vb * cmath.sqrt(3))  # corrente no trafo 2

# --------- corrente de curto na barra de media tensão ----------- #

Z1 = z1r + z1cbpu  # impedância de sequência positiva total
I3ph = ib * 1 / abs(Z1)  # curto trifásico
Fa = cmath.sqrt(1 + 2 * cmath.exp(-2 * cmath.pi * Z1.real / Z1.imag))  # fator de assimetria
I3pha = I3ph * Fa  # corrente de curto assimétrica
I1t = abs(ib * 3 / (2 * Z1 + z0r))  # corrente de curto fase terra
I1ta = I1t * Fa  # corrente de curto fase terra assimétrica
Zf = 3 * rf / zb  # impedância de falta terra
I1tmin = ib * 3 / abs(2 * Z1 + z0r + Zf)  # corrente de falta terra mínima

# --------- corrente de curto na barra de baixa tensão trafo 1----------- #

abs_Z1tf1_bt = ztf1 * vb**2 / (tf1 * zb)  # modulo impedância de sequência positiva em bt do trafo 1
Z1tf1_bt = abs_Z1tf1_bt * (0.1 + 0.995j)  # impedância de sequência positiva em bt do trafo 1 em pu
Z0tf1_bt_tf1 = 0.85 * Z1tf1_bt  # impedância de sequência zero em bt do trafo 1 em pu
Z1total_bt_tf1 = z1r + z1cbpu + Z1tf1_bt  # impedância de sequência positiva total em bt do trafo 1
Z0total_bt_tf1 = Z0tf1_bt_tf1  # impedância de sequência zero total em bt do trafo 1
I3ph_bt_tf1 = ib * 1 / abs(Z1total_bt_tf1)  # curto trifásico
Fa_bt_tf1 = cmath.sqrt(1 + 2 * cmath.exp(-2 * cmath.pi * Z1total_bt_tf1.real / Z1total_bt_tf1.imag))  # fator de assimetria
I3pha_bt_tf1 = I3ph_bt_tf1 * Fa_bt_tf1  # corrente de curto assimétrica
I1t_bt_tf1 = abs(ib * 3 / (2 * Z1total_bt_tf1 + Z0total_bt_tf1))  # corrente de curto fase terra
I1ta_bt_tf1 = I1t * Fa_bt_tf1  # corrente de curto fase terra assimétrica
I1tmin_bt_tf1 = ib * 3 / abs(2 * Z1total_bt_tf1 + Z0total_bt_tf1 + Zf)  # impedância de falta terra mínima

# --------- corrente de curto na barra de baixa tensão trafo 2 ----------- #

abs_Z1tf2_bt = ztf2 * vb**2 / (tf2 * zb)  # modulo impedância de sequência positiva em bt do trafo 2
Z1tf2_bt = abs_Z1tf2_bt * (0.1 + 0.995j)  # impedância de sequência positiva em bt do trafo 2 em pu
Z0tf2_bt = 0.85 * Z1tf2_bt  # impedância de sequência zero em bt do trafo 2 em pu
Z1total_bt_tf2 = z1r + z1cbpu + Z1tf2_bt  # impedância de sequência positiva total em bt do trafo 2
Z0total_bt_tf2 = Z0tf2_bt  # impedância de sequência zero total em bt do trafo 2
I3ph_bt_tf2 = ib * 1 / abs(Z1total_bt_tf2)  # curto trifásico
Fa_bt_tf2 = cmath.sqrt(1 + 2 * cmath.exp(-2 * cmath.pi * Z1total_bt_tf2.real / Z1total_bt_tf2.imag))  # fator de assimetria
I3pha_bt_tf2 = I3ph_bt_tf2 * Fa_bt_tf2  # corrente de curto assimétrica
I1t_bt_tf2 = abs(ib * 3 / (2 * Z1total_bt_tf2 + Z0total_bt_tf2))  # corrente de curto fase terra
I1ta_bt_tf2 = I1t * Fa_bt_tf2  # corrente de curto fase terra assimétrica
I1tmin_bt_tf2 = ib * 3 / abs(2 * Z1total_bt_tf2 + Z0total_bt_tf2 + Zf)  # impedância de falta terra mínima

# --------- dimensionamento do TC ----------- #

Dm = 1400e3  # demanda contratada em W
In = Dm / (vb * 0.92 * cmath.sqrt(3))  # corrente nominal demanda contratada
It = (tf1 + tf2 / (cmath.sqrt(3) * vb))  # corrente nominal dos transformadores
Intc_int1 = I3ph / 20  # Corrente de primeiro critério de curto no TC
Intc_int2 = 2 * In  # Corrente de segundo critério de curto no TC
Intc_int3 = 2 * It  # Corrente de terceiro critério de curto no TC

# --------- corrente de magnetização dos transformadores ----------- #

Imag = intf2 * kinrush2 + intf1  # corrente magnetização dos transformadores

# --------- ponto ANSI dos transformadores ----------- #

IANSI_tf1 = intf1 / ztf1  # corrente magnetização dos transformador 1
TANSI_tf1 = ztf1**2 / 8  # tempo de disparo ANSI transformador 1
IANSI_tf2 = intf2 / ztf2  # corrente magnetização dos transformador 2
TANSI_tf2 = ztf2**2 / 8  # tempo de disparo ANSI transformador 2

# --------- ajustes de curvas de proteção ----------- #
Ipf_inst = Dm / (vb * cmath.sqrt(3))  # corrente de partida da fase demanda
Iif = 1.4 * Imag  # corrente instatânea
Ipn = 0.1 * Ipf_inst  # corrente de partida de neutro
Iin = 0.2 * Iif  # corrente instatânea de fase

# --------- Fatores ----------- #
print('corrente de curto trifásica:', I3ph)
print('corrente de curto trifásica assimétrica:', I3pha)
print('corrente de falta fase terra:', I1t)
print('corrente de falta fase terra assimétrica:', I1ta)
print('corrente de falta terra mínima:', I1tmin)
print('corrente do TC:', Intc_int2, '<', Intc_int1, '<', Intc_int3)  # corrente do TC

