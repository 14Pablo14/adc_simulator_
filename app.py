import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go


st.set_page_config(
    page_title="Simulador ADC",
    layout="wide"
)

st.markdown("""
<style>
/* Ocultar barra superior de Streamlit */
header[data-testid="stHeader"] {
    display: none;
}
<style>
/* Fondo general */
.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #111827 55%, #020617 100%);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #1f2937;
    border-right: 1px solid #374151;
}

/* Título principal */
.main-title {
    background: linear-gradient(90deg, #1a73e8, #0f766e);
    padding: 22px 28px;
    border-radius: 18px;
    margin-bottom: 24px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.30);
    border: 1px solid rgba(255,255,255,0.08);
}

.main-title h1 {
    color: #f9fafb;
    margin: 0;
    font-size: 38px;
}

.main-title p {
    color: #e5e7eb;
    margin-top: 8px;
    font-size: 16px;
}

/* Cards de métricas */
.metric-card {
    background-color: #1f2937;
    padding: 18px;
    border-radius: 16px;
    border: 1px solid #374151;
    box-shadow: 0 4px 14px rgba(0,0,0,0.25);
}

.metric-card:hover {
    border-color: #1a73e8;
    box-shadow: 0 6px 18px rgba(26,115,232,0.18);
}

.metric-label {
    font-size: 13px;
    color: #9ca3af;
    margin-bottom: 6px;
}

.metric-value {
    font-size: 30px;
    font-weight: bold;
    color: #f9fafb;
}

/* Títulos de sección */
.section-title {
    margin-top: 34px;
    margin-bottom: 18px;
}

.section-title h2 {
    color: #f9fafb;
    font-size: 30px;
    margin-bottom: 4px;
}

/* Contenedor de gráficos */
.chart-card {
    background-color: #111827;
    border: 1px solid #374151;
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 30px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.28);
}

/* Alertas de Streamlit un poco más suaves */
div[data-testid="stAlert"] {
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* Texto chico institucional */
.sidebar-footer {
    text-align: center;
    color: #9ca3af;
    font-size: 12px;
    margin-top: 20px;
    padding-top: 10px;
    border-top: 1px solid #374151;
}

/* Logo / texto sidebar */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] label {
    color: #f9fafb;
}

/* Sliders */
.stSlider [data-baseweb="slider"] {
    color: #ef4444;
}
</style>
""", unsafe_allow_html=True)
# -----------------------------
# Título e introducción
# -----------------------------

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


# -----------------------------
# Logo institucional
# -----------------------------

st.sidebar.markdown(
    """
    <div style="text-align: center;">
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.sidebar.columns([1.2, 1, 1.2])

with col2:
    st.image("logo_utn.png", width=90)

st.sidebar.markdown(
    """
    <div style="text-align: center; margin-top: 8px; margin-bottom: 22px;">
        <strong>UTN FRLP</strong><br>
        Comunicación de Datos
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Controles de usuario
# -----------------------------

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

duracion = duracion_ms / 1000

# -----------------------------
# Información teórica desplegable
# -----------------------------

with st.sidebar.expander("Información teórica"):
    st.markdown("""
    ### ¿Qué simula esta aplicación?

    Esta aplicación simula el proceso de **conversión analógica-digital**, también conocido como **ADC**.

    El proceso se divide en tres etapas principales:

    **1. Muestreo**  
    Se toman valores de la señal analógica en determinados instantes de tiempo.  
    Es decir, la señal deja de analizarse de forma continua y pasa a observarse en puntos específicos.

    **2. Cuantización**  
    Cada muestra se aproxima a un nivel discreto según la cantidad de bits elegida.  
    A mayor cantidad de bits, mayor cantidad de niveles disponibles y menor pérdida de precisión.

    **3. Codificación**  
    Los valores cuantizados pueden representarse mediante códigos binarios.  
    Esta etapa permite que la información pueda ser procesada, almacenada o transmitida digitalmente.

    ### Criterio de Nyquist

    La aplicación verifica el **Criterio de Nyquist**, que indica que para reconstruir correctamente una señal, la frecuencia de muestreo debe ser mayor que el doble de la frecuencia máxima de la señal:

    `fs > 2 · fmax`

    Si no se cumple este criterio, puede aparecer **aliasing**, es decir, una representación incorrecta de la señal original.

    ### Error de cuantización

    El **error de cuantización** es la diferencia entre el valor real muestreado y el valor cuantizado.

    En la aplicación se calcula como:

    `Error = Valor muestreado - Valor cuantizado`

    Este error aparece porque una señal analógica puede tomar infinitos valores, mientras que una señal digital solo puede tomar una cantidad limitada de niveles.

    ### Tabla de muestras

    La **tabla de muestras** muestra los valores numéricos obtenidos durante el proceso:

    - Tiempo de cada muestra.
    - Valor muestreado.
    - Valor cuantizado.
    - Error de cuantización.

    Esta tabla permite observar de forma precisa cómo cada punto de la señal analógica fue transformado en un valor digital.

    ### Descarga de datos

    La opción de **descarga CSV** permite exportar la tabla de muestras.

    Esto sirve para analizar los datos fuera de la aplicación, por ejemplo en Excel, Google Sheets o cualquier herramienta de análisis de datos.
    """)

# -----------------------------
# Función para generar señales
# -----------------------------

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

# -----------------------------
# Generación de señal continua
# -----------------------------

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

# -----------------------------
# Muestreo
# -----------------------------

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

# -----------------------------
# Cuantización
# -----------------------------

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

# Pasamos los tiempos a milisegundos para que quede más claro visualmente
t_continuo_ms = t_continuo * 1000
t_muestreo_ms = t_muestreo * 1000

# -----------------------------
# Estado Nyquist
# -----------------------------

st.markdown(
    '<div class="section-title"><h2>Estado del criterio de Nyquist</h2></div>',
    unsafe_allow_html=True
)

frecuencia_nyquist = 2 * frecuencia_senal

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

st.markdown("<div style='margin-top: 16px;'></div>", unsafe_allow_html=True) ##Espacio

if frecuencia_muestreo > frecuencia_nyquist:
    st.success(
        f"Se cumple Nyquist: fs = {frecuencia_muestreo} Hz > 2 · f = {frecuencia_nyquist} Hz"
    )
else:
    st.error(
        f"No se cumple Nyquist: fs = {frecuencia_muestreo} Hz ≤ 2 · f = {frecuencia_nyquist} Hz. Puede aparecer aliasing."
    )

# -----------------------------
# 2. Gráfico señal continua vs muestreada
# -----------------------------

st.header("Señal continua vs señal muestreada")

fig1 = go.Figure()

fig1.add_trace(
    go.Scatter(
        x=t_continuo_ms,
        y=senal_original,
        mode="lines",
        name="Señal continua",
        line=dict(color="#1a73e8", width=2),
        hovertemplate=(
            "Tiempo: %{x:.2f} ms<br>"
            "Amplitud: %{y:.3f}<extra></extra>"
        )
    )
)

fig1.add_trace(
    go.Scatter(
        x=t_muestreo_ms,
        y=senal_muestreada,
        mode="markers",
        name="Puntos muestreados",
        marker=dict(color="#f59e0b", size=7),
        hovertemplate=(
            "Tiempo: %{x:.2f} ms<br>"
            "Valor muestreado: %{y:.3f}<extra></extra>"
        )
    )
)

fig1.update_layout(
    title="Gráfico de señal continua vs. muestreada",
    xaxis_title="Tiempo (ms)",
    yaxis_title="Amplitud",
    hovermode="closest",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.35,
        xanchor="center",
        x=0.5
    ),
    margin=dict(l=40, r=40, t=60, b=80)
)

fig1.update_xaxes(showgrid=True, gridwidth=1, gridcolor="#e5e7eb")
fig1.update_yaxes(showgrid=True, gridwidth=1, gridcolor="#e5e7eb")

with st.container(border=True):
    st.plotly_chart(fig1, use_container_width=True)
# -----------------------------
# 3. Gráfico señal cuantizada
# -----------------------------

st.header("Señal cuantizada")

fig2 = go.Figure()

fig2.add_trace(
    go.Scatter(
        x=t_muestreo_ms,
        y=senal_cuantizada,
        mode="lines+markers",
        name="Señal cuantizada",
        line=dict(color="#10b981", width=2, shape="hv"),
        marker=dict(color="#10b981", size=6),
        hovertemplate=(
            "Tiempo: %{x:.2f} ms<br>"
            "Valor cuantizado: %{y:.3f}<extra></extra>"
        )
    )
)

fig2.update_layout(
    title="Señal cuantizada en escalera digital",
    xaxis_title="Tiempo (ms)",
    yaxis_title="Amplitud",
    hovermode="closest",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.35,
        xanchor="center",
        x=0.5
    ),
    margin=dict(l=40, r=40, t=60, b=80)
)

fig2.update_xaxes(showgrid=True, gridwidth=1, gridcolor="#e5e7eb")
fig2.update_yaxes(showgrid=True, gridwidth=1, gridcolor="#e5e7eb")

with st.container(border=True):
    st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# 4. Gráfico error de cuantización
# -----------------------------

st.header("Error de cuantización")

fig3 = go.Figure()

fig3.add_trace(
    go.Scatter(
        x=t_muestreo_ms,
        y=error_cuantizacion,
        mode="lines+markers",
        name="Error de cuantización",
        line=dict(color="#ef4444", width=2),
        marker=dict(color="#ef4444", size=6),
        hovertemplate=(
            "Tiempo: %{x:.2f} ms<br>"
            "Error: %{y:.6f}<extra></extra>"
        )
    )
)

fig3.add_hline(
    y=0,
    line_dash="dash",
    line_color="#ef4444"
)

fig3.update_layout(
    title="Error entre la señal muestreada y la señal cuantizada",
    xaxis_title="Tiempo (ms)",
    yaxis_title="Error",
    hovermode="closest",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.35,
        xanchor="center",
        x=0.5
    ),
    margin=dict(l=40, r=40, t=60, b=80)
)

fig3.update_xaxes(showgrid=True, gridwidth=1, gridcolor="#e5e7eb")
fig3.update_yaxes(showgrid=True, gridwidth=1, gridcolor="#e5e7eb")

with st.container(border=True):
    st.plotly_chart(fig3, use_container_width=True)


# -----------------------------
# 5. Tabla de muestras
# -----------------------------

st.header("Tabla de muestras")

tabla = pd.DataFrame({
    "Tiempo (ms)": t_muestreo_ms,
    "Valor muestreado": senal_muestreada,
    "Valor cuantizado": senal_cuantizada,
    "Error de cuantización": error_cuantizacion
})

st.dataframe(tabla.head(30))

# -----------------------------
# 6. Descarga CSV
# -----------------------------

st.header("Descarga de datos")

csv = tabla.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Descargar muestras en CSV",
    data=csv,
    file_name="muestras_adc.csv",
    mime="text/csv"
)

# -----------------------------
# Conclusión automática
# -----------------------------
with st.expander("Conclusión automática"):

    periodo_ms = (1 / frecuencia_senal) * 1000

    # Conclusión sobre Nyquist
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

    # Información adicional de la señal
    st.info(
        f"El período de la señal es de aproximadamente {periodo_ms:.2f} ms. "
        f"Durante los {duracion_ms} ms analizados, el sistema tomó {cantidad_muestras} muestras."
    )

    # Conclusión sobre cuantización
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

    # Conclusión sobre error
    st.write(
        f"El error promedio de cuantización obtenido es de {error_promedio:.6f}. "
        "Este valor representa la diferencia promedio entre cada muestra original y su valor cuantizado."
    )