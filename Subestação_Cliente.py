# --------- informações da subestação ----------- #

# cabo de entrada
cb = 35  # cabo bitola media tensão
r_un_cb = 0.67 # Valor da resistência do cabo em (ohm/km) procurar valor na tabela do fabricante
x_un_cb = 0.147 # Valor da reatância do cabo em (ohm/km) procurar valor na tabela do fabricante
lcb = 2500  # comprimento do cabo

# transformadores
tf1 = (45+45+45+75+150)*1e3  # potência do trafo 1
ztf1 = 0.055  # impedância percentual do trafo 1
kinrush1 = 10  # fator k da corrente de magnetização do trafo 1
tf2 = (112.5+112.5)*1e3  # potência do trafo 2
ztf2 = 0.045  # impedância percentual do trafo 2
kinrush2 = 8  # fator k da corrente de magnetização do trafo 2