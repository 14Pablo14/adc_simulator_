import streamlit as st


def mostrar_sidebar():
    # Logo institucional
    st.sidebar.markdown(
        """
        <div style="text-align: center;">
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.sidebar.columns([1.2, 1, 1.2])

    with col2:
        st.image("assets/logo_utn.png", width=90)

    st.sidebar.markdown(
        """
        <div style="text-align: center; margin-top: 8px; margin-bottom: 22px;">
            <strong>UTN FRLP</strong><br>
            Comunicación de Datos
        </div>
        """,
        unsafe_allow_html=True
    )

    # Controles de usuario
    st.sidebar.markdown("---")
    st.sidebar.header("Parámetros de la señal")

    tipo_senal = st.sidebar.selectbox(
        "Tipo de señal",
        ["Senoidal", "Cuadrada", "Triangular"]
    )

    amplitud = st.sidebar.slider(
        "Amplitud",
        min_value=1.0,
        max_value=10.0,
        value=1.0,
        step=0.5
    )

    frecuencia_senal = st.sidebar.slider(
        "Frecuencia de la señal (Hz)",
        min_value=1,
        max_value=100,
        value=64,
        step=1
    )

    frecuencia_muestreo = st.sidebar.slider(
        "Frecuencia de muestreo fs (Hz)",
        min_value=5,
        max_value=1000,
        value=500,
        step=5
    )

    bits = st.sidebar.selectbox(
        "Bits de cuantización",
        [2, 4, 8, 16, 24],
        index=1
    )

    duracion_ms = st.sidebar.slider(
        "Duración de la señal (milisegundos)",
        min_value=10,
        max_value=500,
        value=50,
        step=10
    )

    agregar_ruido = st.sidebar.checkbox("Agregar ruido blanco")

    with st.sidebar.expander("Información teórica"):
        st.markdown("""
        ### ¿Qué simula esta aplicación?

        Esta aplicación simula el proceso de **conversión analógica-digital**, también conocido como **ADC**.

        El proceso se divide en tres etapas principales:

        **1. Muestreo**  
        Se toman valores de la señal analógica en determinados instantes de tiempo.

        **2. Cuantización**  
        Cada muestra se aproxima a un nivel discreto según la cantidad de bits elegida.

        **3. Codificación**  
        Los valores cuantizados pueden representarse mediante códigos binarios.

        ### Criterio de Nyquist

        Para reconstruir correctamente una señal, la frecuencia de muestreo debe ser mayor que el doble de la frecuencia máxima:

        `fs > 2 · fmax`

        Si no se cumple este criterio, puede aparecer **aliasing**.

        ### Error de cuantización

        `Error = Valor muestreado - Valor cuantizado`

        ### Tabla de muestras

        Muestra:
        - Tiempo de cada muestra.
        - Valor muestreado.
        - Valor cuantizado.
        - Error de cuantización.

        ### Descarga de datos

        Permite exportar los datos en formato CSV.
        """)

    return {
        "tipo_senal": tipo_senal,
        "amplitud": amplitud,
        "frecuencia_senal": frecuencia_senal,
        "frecuencia_muestreo": frecuencia_muestreo,
        "bits": bits,
        "duracion_ms": duracion_ms,
        "agregar_ruido": agregar_ruido
    }