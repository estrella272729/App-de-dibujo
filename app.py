import streamlit as st
import sys
import subprocess
import importlib
import traceback
from PIL import Image
import io
import base64

st.set_page_config(page_title="App de Dibujo (con fallback)", layout="centered")

st.title("App de Dibujo — intento de import dinámico")

# -------------------------
# Intentar importar streamlit_drawable_canvas
# -------------------------
canvas_available = False
st.write("Comprobando dependencia `streamlit_drawable_canvas`...")

try:
    from streamlit_drawable_canvas import st_canvas
    canvas_available = True
    st.success("Import OK: streamlit_drawable_canvas disponible.")
except Exception as e:
    st.warning("Import fallido: streamlit_drawable_canvas no encontrado.")
    st.text("Intentando instalar desde GitHub (esto tarda algunos segundos)...")
    try:
        # Ejecutar pip install desde git
        subprocess.check_call([sys.executable, "-m", "pip", "install", "git+https://github.com/andfanilo/streamlit-drawable-canvas.git"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        # reintentar la importación
        importlib.invalidate_caches()
        from streamlit_drawable_canvas import st_canvas
        canvas_available = True
        st.success("Instalación e importación exitosas desde GitHub.")
    except Exception as e2:
        st.error("No fue posible instalar/importar streamlit_drawable_canvas automáticamente.")
        st.text("Error de instalación/importación (traza):")
        st.text(traceback.format_exc())

# -------------------------
# Si está disponible: interfaz con canvas
# -------------------------
if canvas_available:
    st.markdown("### 🎨 Lienzo interactivo (streamlit_drawable_canvas)")
    from streamlit_drawable_canvas import st_canvas  # re-import por si acaso

    # Controles
    stroke_width = st.sidebar.slider("Grosor del pincel", 1, 25, 5)
    stroke_color = st.sidebar.color_picker("Color del pincel", "#00FFAA")
    bg_color = st.sidebar.color_picker("Color del fondo", "#000000")
    realtime_update = st.sidebar.checkbox("Actualizar en tiempo real", True)
    drawing_mode = st.sidebar.selectbox("Modo de dibujo", ("freedraw", "line", "rect", "circle", "transform"))

    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 0)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        update_streamlit=realtime_update,
        height=400,
        width=600,
        drawing_mode=drawing_mode,
        key="canvas",
    )

    col1, col2 = st.columns(2)
    if col1.button("🧹 Limpiar"):
        st.experimental_rerun()

    if col2.button("💾 Descargar PNG"):
        if canvas_result.image_data is not None:
            img = Image.fromarray((canvas_result.image_data).astype("uint8"))
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            b64 = base64.b64encode(buf.getvalue()).decode()
            href = f'<a href="data:file/png;base64,{b64}" download="mi_dibujo.png">Descargar imagen</a>'
            st.markdown(href, unsafe_allow_html=True)
        else:
            st.warning("Dibuja algo primero para poder descargar.")
else:
    # -------------------------
    # FALLBACK: interfaz con subida de imagen + anotación mínima
    # -------------------------
    st.markdown("### ⚠️ Canvas no disponible — usando modo alternativo")
    st.info("El componente interactivo no se pudo cargar. Puedes subir una imagen y dibujar/editarla localmente, o volver cuando `streamlit_drawable_canvas` esté instalado en tu entorno (revisa requirements.txt).")

    uploaded = st.file_uploader("Sube una imagen (o arrastra)", type=["png","jpg","jpeg"])
    if uploaded:
        img = Image.open(uploaded).convert("RGBA")
        st.image(img, caption="Imagen subida", use_container_width=True)
        st.markdown("Opciones de fallback:")
        if st.button("Descargar tal cual"):
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            b64 = base64.b64encode(buf.getvalue()).decode()
            href = f'<a href="data:file/png;base64,{b64}" download="imagen_subida.png">Descargar imagen</a>'
            st.markdown(href, unsafe_allow_html=True)

    st.markdown("---")
    st.caption("Para reinstalar el canvas en Streamlit Cloud: añade en requirements.txt la línea\n`git+https://github.com/andfanilo/streamlit-drawable-canvas.git` y reconstruye la app (Manage → Rebuild).")

