import streamlit as st
from streamlit_drawable_canvas import st_canvas  

# Configuración de la página
st.set_page_config(page_title="Tablero para dibujo", layout="centered")

# Título principal
st.title("🖌️ Tablero para dibujo")

# Barra lateral con las propiedades del tablero
with st.sidebar:
    st.subheader("Propiedades del Tablero")

    # Dimensiones del canvas
    st.subheader("Dimensiones del Tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 400, 50)

    # Selector de herramienta
    drawing_mode = st.selectbox(
        "Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point")
    )

    # Ancho de línea
    stroke_width = st.slider("Selecciona el ancho de línea", 1, 30, 22)

    # Color del trazo
    stroke_color = st.color_picker("Color de trazo", "#00FF66")

    # Color de fondo
    bg_color = st.color_picker("Color de fondo", "#000000")

# Crear el canvas para dibujar
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Color de relleno (transparente)
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",  # Evita errores de actualización
)

st.markdown("🖍️ Usa el panel lateral para ajustar las herramientas y colores.")


