# Dados de entrada
niveis_curto_circuito = {
    "Icc3f": 1.619,
    "Icc3fassim": 1.684,
    "Icc2f": 1.402,
    "Iccftmax": 1.169,
    "Iccftmin": 183,
}
impedancias = {
    "Z1": complex(1.4507, 2.1381),
    "Z0": complex(1.8070, 5.3744),
}

# Ajustes de proteção do religador
rele = {
    "tipo": "351-R",
    "rtc": 500,
    "fase": {"pickup": 230, "tap_inst": 895, "curva": "DEF_05"},
    "neutro": {"pickup": 25, "tap_inst": 550},
    "religamentos": [5, 20, 40]  # em segundos
}



