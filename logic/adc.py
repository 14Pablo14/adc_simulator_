import numpy as np
import pandas as pd

from logic.signals import generar_senal


def procesar_adc(tipo_senal, amplitud, frecuencia_senal, frecuencia_muestreo, bits, duracion_ms, agregar_ruido):
    duracion = duracion_ms / 1000

    # Señal continua
    t_continuo = np.linspace(0, duracion, 5000)

    senal_original = generar_senal(
        tipo_senal,
        amplitud,
        frecuencia_senal,
        t_continuo
    )

    if agregar_ruido:
        ruido = np.random.normal(0, amplitud * 0.1, len(t_continuo))
        senal_original = senal_original + ruido

    # Muestreo
    cantidad_muestras = max(2, int(frecuencia_muestreo * duracion))

    t_muestreo = np.linspace(0, duracion, cantidad_muestras)

    senal_muestreada = generar_senal(
        tipo_senal,
        amplitud,
        frecuencia_senal,
        t_muestreo
    )

    if agregar_ruido:
        ruido_muestreo = np.random.normal(0, amplitud * 0.1, len(t_muestreo))
        senal_muestreada = senal_muestreada + ruido_muestreo

    # Cuantización
    niveles = 2 ** bits

    valor_min = -amplitud
    valor_max = amplitud

    senal_normalizada = (senal_muestreada - valor_min) / (valor_max - valor_min)
    senal_normalizada = np.clip(senal_normalizada, 0, 1)

    senal_cuantizada_normalizada = (
        np.round(senal_normalizada * (niveles - 1)) / (niveles - 1)
    )

    senal_cuantizada = (
        senal_cuantizada_normalizada * (valor_max - valor_min) + valor_min
    )

    error_cuantizacion = senal_muestreada - senal_cuantizada
    error_promedio = np.mean(np.abs(error_cuantizacion))

    # Tiempo en milisegundos
    t_continuo_ms = t_continuo * 1000
    t_muestreo_ms = t_muestreo * 1000

    frecuencia_nyquist = 2 * frecuencia_senal

    periodo_ms = (1 / frecuencia_senal) * 1000

    tabla = pd.DataFrame({
        "Tiempo (ms)": t_muestreo_ms,
        "Valor muestreado": senal_muestreada,
        "Valor cuantizado": senal_cuantizada,
        "Error de cuantización": error_cuantizacion
    })

    return {
        "duracion": duracion,
        "t_continuo_ms": t_continuo_ms,
        "t_muestreo_ms": t_muestreo_ms,
        "senal_original": senal_original,
        "senal_muestreada": senal_muestreada,
        "senal_cuantizada": senal_cuantizada,
        "error_cuantizacion": error_cuantizacion,
        "error_promedio": error_promedio,
        "niveles": niveles,
        "frecuencia_nyquist": frecuencia_nyquist,
        "cantidad_muestras": cantidad_muestras,
        "periodo_ms": periodo_ms,
        "tabla": tabla
    }