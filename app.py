import streamlit as st

from styles.styles import cargar_estilos
from ui.sidebar import mostrar_sidebar
from ui.components import (
    mostrar_titulo,
    mostrar_estado_nyquist,
    mostrar_tabla_y_descarga,
    mostrar_conclusion
)
from ui.charts import (
    mostrar_grafico_senal,
    mostrar_grafico_cuantizada,
    mostrar_grafico_error
)
from logic.adc import procesar_adc


st.set_page_config(
    page_title="Simulador ADC",
    page_icon="assets/logo_utn.png",
    layout="wide"
)

cargar_estilos()

mostrar_titulo()

parametros = mostrar_sidebar()

resultados = procesar_adc(
    tipo_senal=parametros["tipo_senal"],
    amplitud=parametros["amplitud"],
    frecuencia_senal=parametros["frecuencia_senal"],
    frecuencia_muestreo=parametros["frecuencia_muestreo"],
    bits=parametros["bits"],
    duracion_ms=parametros["duracion_ms"],
    agregar_ruido=parametros["agregar_ruido"]
)

mostrar_estado_nyquist(
    frecuencia_senal=parametros["frecuencia_senal"],
    frecuencia_muestreo=parametros["frecuencia_muestreo"],
    frecuencia_nyquist=resultados["frecuencia_nyquist"],
    niveles=resultados["niveles"],
    error_promedio=resultados["error_promedio"]
)

mostrar_grafico_senal(
    t_continuo_ms=resultados["t_continuo_ms"],
    senal_original=resultados["senal_original"],
    t_muestreo_ms=resultados["t_muestreo_ms"],
    senal_muestreada=resultados["senal_muestreada"]
)

mostrar_grafico_cuantizada(
    t_muestreo_ms=resultados["t_muestreo_ms"],
    senal_cuantizada=resultados["senal_cuantizada"]
)

mostrar_grafico_error(
    t_muestreo_ms=resultados["t_muestreo_ms"],
    error_cuantizacion=resultados["error_cuantizacion"]
)

mostrar_tabla_y_descarga(resultados["tabla"])

mostrar_conclusion(parametros, resultados)