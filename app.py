import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
from PIL import Image
import tensorflow as tf

st.title("🖌️ Tablero para dibujar y reconocer")

# Propiedades del tablero
with st.sidebar:
    st.subheader("Propiedades del Tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)
    drawing_mode = st.selectbox(
        "Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )
    stroke_width = st.slider("Selecciona el ancho de línea", 1, 30, 15)
    stroke_color = st.color_picker("Color de trazo", "#FFFFFF")
    bg_color = st.color_picker("Color de fondo", "#000000")

# Crear el lienzo
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

# Procesar el dibujo
if canvas_result.image_data is not None:
    img = Image.fromarray((canvas_result.image_data).astype("uint8"))
    img = img.convert("L")  # convertir a blanco y negro
    img = img.resize((28, 28))  # tamaño estándar para MNIST
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    st.image(img, caption="Dibujo procesado", width=150)

    # Cargar modelo
    model = tf.keras.models.load_model("modelo_dibujos.h5")

    # Predicción
    pred = model.predict(img_array)
    st.write("🔮 Predicción:", np.argmax(pred))
