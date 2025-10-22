import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io
import base64

# -------------------------------
# CONFIGURACIÓN INICIAL
# -------------------------------
st.set_page_config(page_title="App de Dibujo Espacial 🎨🚀", layout="centered")

st.title("🎨 Lienzo Espacial de Dibujo 🚀")
st.markdown("""
Bienvenido al **Laboratorio Creativo Espacial**.  
Aquí puedes dibujar tus ideas, bocetar planetas o diseñar tu próxima nave intergaláctica.  
Usa el lienzo interactivo de abajo y deja volar tu imaginación.
""")

# -------------------------------
# CONTROLES LATERALES
# -------------------------------
st.sidebar.header("🎛️ Controles del Lienzo")

stroke_width = st.sidebar.slider("Grosor del pincel", 1, 25, 5)
stroke_color = st.sidebar.color_picker("Color del pincel", "#00FFAA")
bg_color = st.sidebar.color_picker("Color del fondo", "#000000")

realtime_update = st.sidebar.checkbox("Actualizar en tiempo real", True)
drawing_mode = st.sidebar.selectbox(
    "Modo de dibujo", ("freedraw", "line", "rect", "circle", "transform")
)

st.sidebar.markdown("---")
st.sidebar.caption("💡 Consejo: usa el botón de abajo para limpiar o guardar tu dibujo.")

# -------------------------------
# CANVAS DE DIBUJO
# -------------------------------
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0)",  # Relleno transparente
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    update_streamlit=realtime_update,
    height=400,
    width=600,
    drawing_mode=drawing_mode,
    key="canvas",
)

# -------------------------------
# BOTONES DE ACCIÓN
# -------------------------------
col1, col2 = st.columns(2)

# Limpiar el lienzo
if col1.button("🧹 Limpiar Lienzo"):
    st.experimental_rerun()

# Guardar dibujo como imagen
if col2.button("💾 Guardar Dibujo"):
    if canvas_result.image_data is not None:
        img = Image.fromarray((canvas_result.image_data).astype("uint8"))
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        b64 = base64.b64encode(byte_im).decode()
        href = f'<a href="data:file/png;base64,{b64}" download="dibujo_espacial.png">📥 Descargar tu dibujo</a>'
        st.markdown(href, unsafe_allow_html=True)
    else:
        st.warning("Primero dibuja algo en el lienzo antes de guardar.")

# -------------------------------
# MENSAJE FINAL
# -------------------------------
st.markdown("---")
st.caption("👩‍🚀 Creado para artistas espaciales con Streamlit y amor galáctico 💫")


