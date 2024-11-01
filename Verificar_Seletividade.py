# Verificações de seletividade
def verificar_seletividade(corrente_curto_trifasica, pickup_fase, corrente_curto_trifasica_assimetrica,
                       corrente_falta_fase_terra, pickup_neutro, corrente_tc, corrente_falta_terra_minima):
    print("Verificações de Seletividade:")
    
    # Verificação do relé de fase
    if corrente_curto_trifasica > pickup_fase:
        print(f"Corrente de curto trifásica ({corrente_curto_trifasica:.2f} A) > Pick-up de fase ({pickup_fase} A): Relé pode atuar.")
    else:
        print(f"Corrente de curto trifásica ({corrente_curto_trifasica:.2f} A) <= Pick-up de fase ({pickup_fase} A): Relé não atua.")
    
    if corrente_curto_trifasica_assimetrica > pickup_fase:
        print(f"Corrente de curto trifásica assimétrica ({corrente_curto_trifasica_assimetrica:.2f} A) > Pick-up de fase ({pickup_fase} A): Relé pode atuar.")
    
    # Verificação do relé neutro
    if corrente_falta_fase_terra > pickup_neutro:
        print(f"Corrente de falta fase-terra ({corrente_falta_fase_terra:.2f} A) > Pick-up neutro ({pickup_neutro} A): Relé pode atuar.")
    else:
        print(f"Corrente de falta fase-terra ({corrente_falta_fase_terra:.2f} A) <= Pick-up neutro ({pickup_neutro} A): Relé não atua.")

    # Verificação da corrente do TC
    if corrente_tc < corrente_falta_terra_minima:
        print(f"Corrente do TC ({corrente_tc:.2f} A) < Corrente mínima de falta terra ({corrente_falta_terra_minima:.2f} A): Seletividade mantida.")
    else:
        print(f"Corrente do TC ({corrente_tc:.2f} A) >= Corrente mínima de falta terra ({corrente_falta_terra_minima:.2f} A): Seletividade comprometida.")

