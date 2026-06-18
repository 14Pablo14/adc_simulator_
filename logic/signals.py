import numpy as np


def generar_senal(tipo, amplitud, frecuencia, tiempo):
    if tipo == "Senoidal":
        return amplitud * np.sin(2 * np.pi * frecuencia * tiempo)

    elif tipo == "Cuadrada":
        return amplitud * np.sign(
            np.sin(2 * np.pi * frecuencia * tiempo)
        )

    else:
        return amplitud * (2 / np.pi) * np.arcsin(
            np.sin(2 * np.pi * frecuencia * tiempo)
        )