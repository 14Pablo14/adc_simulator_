import streamlit as st


def cargar_estilos():
    st.markdown("""
    <style>
    /* Ocultar barra superior de Streamlit */
    header[data-testid="stHeader"] {
        display: none;
    }

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

    /* Alertas de Streamlit */
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