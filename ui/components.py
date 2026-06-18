import streamlit as st


def mostrar_titulo():
    st.title("Simulador de Conversión Analógica-Digital")

    st.markdown("""
    <p style="
        font-size: 18px;
        color: #C0D8E1;
        margin-top: -10px;
        margin-bottom: 35px;
    ">
    Visualización interactiva del proceso de muestreo, cuantización y detección de aliasing.
    </p>
    """, unsafe_allow_html=True)


def mostrar_estado_nyquist(frecuencia_senal, frecuencia_muestreo, frecuencia_nyquist, niveles, error_promedio):
    st.markdown(
        '<div class="section-title"><h2>Estado del criterio de Nyquist</h2></div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Frecuencia de la señal</div>
            <div class="metric-value">{frecuencia_senal} Hz</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Frecuencia de muestreo</div>
            <div class="metric-value">{frecuencia_muestreo} Hz</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Niveles de cuantización</div>
            <div class="metric-value">{niveles}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Error promedio</div>
            <div class="metric-value">{error_promedio:.6f}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 16px;'></div>", unsafe_allow_html=True)

    if frecuencia_muestreo > frecuencia_nyquist:
        st.success(
            f"Se cumple Nyquist: fs = {frecuencia_muestreo} Hz > 2 · f = {frecuencia_nyquist} Hz"
        )
    else:
        st.error(
            f"No se cumple Nyquist: fs = {frecuencia_muestreo} Hz ≤ 2 · f = {frecuencia_nyquist} Hz. Puede aparecer aliasing."
        )


def mostrar_tabla_y_descarga(tabla):
    st.header("Tabla de muestras")
    st.dataframe(tabla.head(30))

    st.header("Descarga de datos")

    csv = tabla.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Descargar muestras en CSV",
        data=csv,
        file_name="muestras_adc.csv",
        mime="text/csv"
    )


def mostrar_conclusion(parametros, resultados):
    frecuencia_senal = parametros["frecuencia_senal"]
    frecuencia_muestreo = parametros["frecuencia_muestreo"]
    bits = parametros["bits"]
    duracion_ms = parametros["duracion_ms"]

    frecuencia_nyquist = resultados["frecuencia_nyquist"]
    periodo_ms = resultados["periodo_ms"]
    cantidad_muestras = resultados["cantidad_muestras"]
    niveles = resultados["niveles"]
    error_promedio = resultados["error_promedio"]

    with st.expander("Conclusión automática"):

        if frecuencia_muestreo > frecuencia_nyquist:
            st.success(
                f"La señal cumple el criterio de Nyquist, ya que la frecuencia de muestreo es de "
                f"{frecuencia_muestreo} Hz y supera el mínimo requerido de {frecuencia_nyquist} Hz."
            )

            st.write(
                f"Esto significa que una señal de {frecuencia_senal} Hz puede representarse correctamente "
                "con la frecuencia de muestreo seleccionada."
            )
        else:
            st.error(
                f"La señal no cumple el criterio de Nyquist, ya que la frecuencia de muestreo es de "
                f"{frecuencia_muestreo} Hz y debería ser mayor que {frecuencia_nyquist} Hz."
            )

            st.write(
                "En este caso puede aparecer aliasing, lo que provoca que la señal digitalizada "
                "no represente correctamente a la señal analógica original."
            )

        st.info(
            f"El período de la señal es de aproximadamente {periodo_ms:.2f} ms. "
            f"Durante los {duracion_ms} ms analizados, el sistema tomó {cantidad_muestras} muestras."
        )

        if bits <= 4:
            st.warning(
                f"La cuantización utiliza {bits} bits, es decir, {niveles} niveles posibles. "
                "Es una cantidad baja de niveles, por lo que la señal cuantizada puede verse más escalonada "
                "y el error de cuantización puede ser mayor."
            )

        elif bits <= 8:
            st.info(
                f"La cuantización utiliza {bits} bits, es decir, {niveles} niveles posibles. "
                "Esto permite una representación intermedia de la amplitud, con un error de cuantización moderado."
            )

        else:
            st.success(
                f"La cuantización utiliza {bits} bits, es decir, {niveles} niveles posibles. "
                "Esto permite representar la amplitud con mayor precisión y reducir el error de cuantización."
            )

        st.write(
            f"El error promedio de cuantización obtenido es de {error_promedio:.6f}. "
            "Este valor representa la diferencia promedio entre cada muestra original y su valor cuantizado."
        )