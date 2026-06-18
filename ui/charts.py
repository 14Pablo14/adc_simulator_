import streamlit as st
import plotly.graph_objects as go


def mostrar_grafico_senal(t_continuo_ms, senal_original, t_muestreo_ms, senal_muestreada):
    st.header("Señal continua vs señal muestreada")

    fig = go.Figure()

    fig.add_trace(
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

    fig.add_trace(
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

    fig.update_layout(
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

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="#e5e7eb")
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="#e5e7eb")

    with st.container(border=True):
        st.plotly_chart(fig, use_container_width=True)


def mostrar_grafico_cuantizada(t_muestreo_ms, senal_cuantizada):
    st.header("Señal cuantizada")

    fig = go.Figure()

    fig.add_trace(
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

    fig.update_layout(
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

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="#e5e7eb")
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="#e5e7eb")

    with st.container(border=True):
        st.plotly_chart(fig, use_container_width=True)


def mostrar_grafico_error(t_muestreo_ms, error_cuantizacion):
    st.header("Error de cuantización")

    fig = go.Figure()

    fig.add_trace(
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

    fig.add_hline(
        y=0,
        line_dash="dash",
        line_color="#ef4444"
    )

    fig.update_layout(
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

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="#e5e7eb")
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="#e5e7eb")

    with st.container(border=True):
        st.plotly_chart(fig, use_container_width=True)