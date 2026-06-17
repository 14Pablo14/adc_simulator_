# Simulador ADC - Comunicación de Datos

Aplicación web desarrollada en Python y Streamlit para simular el proceso de Conversión Analógica-Digital (ADC), permitiendo visualizar el muestreo, la cuantización y la verificación del criterio de Nyquist de forma interactiva.

## Integrantes

- Rey Lautaro
- Quiroz Mallon Juan Pablo
- Selinger Juanita
- Beneforti Franco

## Tecnologías utilizadas

- Python 3.11+
- Streamlit
- NumPy
- Pandas
- Plotly

## Funcionalidades

- Generación de señales:
  - Senoidal
  - Cuadrada
  - Triangular

- Configuración de:
  - Amplitud
  - Frecuencia de la señal
  - Frecuencia de muestreo
  - Bits de cuantización
  - Duración de la señal
  - Ruido blanco

- Verificación automática del criterio de Nyquist.
- Visualización interactiva de la señal continua y muestreada.
- Visualización de la señal cuantizada.
- Visualización del error de cuantización.
- Tabla de muestras generadas.
- Descarga de resultados en formato CSV.
- Conclusión automática basada en los parámetros seleccionados.

## Conceptos teóricos implementados

### Muestreo

Obtención de muestras discretas de una señal analógica.

### Cuantización

Conversión de valores continuos a niveles discretos.

Número de niveles:

L = 2^n

donde:

- L = niveles de cuantización
- n = cantidad de bits

### Criterio de Nyquist

Para evitar aliasing:

fs > 2 · fmax

donde:

- fs = frecuencia de muestreo
- fmax = frecuencia máxima de la señal

### Error de cuantización

Error producido al aproximar una muestra al nivel digital más cercano.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/14Pablo14/adc_simulator_
cd adc-simulador
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar la aplicación

```bash
streamlit run app.py
```

## Estructura del proyecto

```text
adc-simulador/
│
├── app.py
├── requirements.txt
├── README.md
├── logo_utn.png
├── .gitignore
└── venv/
```

## Despliegue

Aplicación desplegada mediante Streamlit Community Cloud.

## Materia

Comunicación de Datos  
UTN Facultad Regional La Plata
