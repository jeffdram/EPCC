import numpy as np

# Valores iniciais Concessionária
Fe_1 = 0.01
Iac_1 = 3
Iinst_1 = 15
Tms_1 = 1.5
Tint_1=0.15
I_1 = Iac_1 * (1 + Fe_1)
mi_1 = (13.5 / ((I_1 / Iac_1) - 1)) * Tms_1

# Listas para armazenar os valores
I_values_1 = []
mi_values_1 = []
I_values_1.append(I_1)
mi_values_1.append(mi_1)

# Loop para 239 iterações
for i in range(239):
    I_1 = I_1 * (1 + Fe_1)
    mi_1 = (13.5 / ((I_1/ Iac_1) - 1)) * Tms_1
    if I_1 < Iinst_1:
        mi_50_51_1=mi_1
    else:
        mi_50_51_1=Tint_1
    
    # Armazenar os valores nas listas
    I_values_1.append(I_1)
    mi_values_1.append(mi_50_51_1)

tempos_atuacao_1 = np.array(mi_values_1)

# Valores iniciais Cliente
Fe_2 = 0.03
Iac_2 = 0.95
Iinst_2 = 12.5
Tms_2 = 0.72
Tint_2=0.1
I_2 = Iac_2 * (1 + Fe_2)
mi_2 = (13.5 / ((I_2 / Iac_2) - 1)) * Tms_2

# Listas para armazenar os valores
I_values_2 = []
mi_values_2 = []
I_values_2.append(I_2)
mi_values_2.append(mi_2)

# Loop para 239 iterações
for j in range(239):
    I_2 = I_2 * (1 + Fe_2)
    mi_2 = (13.5 / ((I_2 / Iac_2) - 1)) * Tms_2
    if I_2 < Iinst_2:
        mi_50_51_2=mi_2
    else:
        mi_50_51_2=Tint_2
    
    # Armazenar os valores nas listas
    I_values_2.append(I_2)
    mi_values_2.append(mi_50_51_2)

tempos_atuacao_2 = np.array(mi_values_2)

# Tempos de atuação correspondentes em segundos
tempos_atuacao = [1, 2, 3, 4, 5, 6, 7, 8]  # Ajuste conforme necessário
