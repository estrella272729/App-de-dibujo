import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io
import base64

# --- Configuración general ---
st.set_page_config(page_title="🎨 Taller del Artista Digital", layout="centered")
st.title("🎨 Taller del Artista Digital")
st.write("Bienvenido a tu espacio creativo. Dibuja, explora y guarda tus obras.")

# --- Sidebar con controles ---
with st.sidebar:
    st.header("🧰 Propiedades del Lienzo")
    
    # Dimensiones
    canvas_width = st.slider("Ancho del lienzo", 300, 1000, 600, 50)
    canvas_height = st.slider("Alto del lienzo", 300, 800, 400, 50)
    
    # Herramienta
    drawing_mode = st.selectbox(
        "✏️ Herramienta de Dibujo",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point")
    )
    
    # Grosor de línea
    stroke_width = st.slider("Grosor del trazo", 1, 30, 5)
    
    # Color de línea
    stroke_color = st.color_picker("🎨 Color del trazo", "#000000")
    
    # Fondo
    bg_color = st.color_picker("🌈 Color de fondo", "#FFFFFF")
    
    # Botones de acción
    st.markdown("---")
    st.subheader("💾 Acciones")
    save_btn = st.button("Guardar dibujo")
    clear_btn = st.button("Limpiar lienzo")

# --- Crear el lienzo ---
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.2)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",
)

# --- Funciones extra ---
if clear_btn:
    st.experimental_rerun()

# Guardar imagen si se presiona el botón
if save_btn and canvas_result.image_data is not None:
    image = Image.fromarray(canvas_result.image_data.astype("uint8"), "RGBA")
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    b64 = base64.b64encode(byte_im).decode()
    href = f'<a href="data:file/png;base64,{b64}" download="mi_obra.png">Descargar imagen 🎨</a>'
    st.markdown(href, unsafe_allow_html=True)
    st.success("¡Tu obra está lista para descargar!")

# Texto motivacional
st.markdown("---")
st.info("✨ Consejo: Usa diferentes colores y formas para explorar tu creatividad.")

