import streamlit as st
from st_canvas import st_canvas
from PIL import Image
import numpy as np

# Configuración de la página
st.set_page_config(page_title='Tablero Inteligente', layout="wide")
st.title('🖌️ Tablero Inteligente: Historias y Chistes con tus Dibujos')

# Panel lateral con controles
with st.sidebar:
    st.subheader("🎨 Propiedades del Tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 400, 50)

    drawing_mode = st.selectbox(
        "Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
    stroke_color = st.color_picker("Color de trazo", "#00FF00")
    bg_color = st.color_picker("Color de fondo", "#000000")

# Canvas para dibujar
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",
)

st.divider()
st.subheader("✨ Opciones creativas")

# Texto de descripción del dibujo
descripcion = st.text_area("✏️ Describe brevemente lo que dibujaste:")

# Generar historia
if st.button("📚 Crear historia infantil"):
    if descripcion.strip() == "":
        st.warning("Por favor escribe una breve descripción del dibujo antes de generar la historia.")
    else:
        historia = f"Había una vez un dibujo llamado '{descripcion}'. En un lugar lleno de colores y risas, este dibujo cobraba vida cada vez que alguien lo miraba con cariño. Un día, decidió emprender una aventura mágica en busca de nuevos amigos. 🌈✨"
        st.markdown("**📖 Tu historia:**")
        st.write(historia)

# Generar chiste
st.subheader("😂 Generador de chistes")
estilo = st.selectbox(
    "Elige un estilo de chiste",
    ["Chiste clásico", "Chiste de niños", "Chiste tipo papá", "Chiste absurdo"]
)

if st.button("🎭 Crear chiste"):
    if descripcion.strip() == "":
        st.warning("Por favor escribe una breve descripción del dibujo antes de generar el chiste.")
    else:
        if estilo == "Chiste clásico":
            chiste = f"¿Sabes qué dijo el dibujo de {descripcion}? ¡‘No me borres, que tengo línea de vida!’ 😂"
        elif estilo == "Chiste de niños":
            chiste = f"¿Qué hace un {descripcion} cuando tiene hambre? ¡Pide un crayón con papas! 🍟🤣"
        elif estilo == "Chiste tipo papá":
            chiste = f"¿Por qué el {descripcion} nunca se pierde? Porque siempre sigue las líneas. 😎"
        else:
            chiste = f"El {descripcion} decidió ir a la luna con un lápiz gigante... y ahora dibuja cráteres. 🌕🖊️"
        
        st.markdown("**🤣 Tu chiste:**")
        st.write(chiste)

