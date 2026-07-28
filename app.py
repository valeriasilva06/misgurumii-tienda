import streamlit as st

# Configuración de la página
st.set_page_config(page_title="@misgurumii - Tienda Oficial", page_icon="🧶", layout="wide")

# Estilos CSS personalizados para darle un toque morado y diseño de tarjetas
st.markdown("""
    <style>
    /* Estilo general y tipografía */
    .main {
        background-color: #faf7fc;
    }
    
    /* Tarjetas de productos */
    .product-card {
        background-color: #ffffff;
        border: 2px solid #e8dff5;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(114, 9, 183, 0.05);
    }
    
    /* Botones personalizados con tono morado */
    .stButton>button {
        background-color: #7209b7;
        color: white;
        border-radius: 10px;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #560bad;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# "Base de datos" temporal en memoria
if "productos" not in st.session_state:
    st.session_state.productos = [
        {
            "nombre": "Patrón Osito tierno (PDF)",
            "categoria": "Tejidos",
            "precio": 5.00,
            "descripcion": "PDF paso a paso para tejer este tierno osito.",
            "tipo": "Digital"
        },
        {
            "nombre": "Amigurumi Llavero de Pollito",
            "categoria": "Amigurumis, Llaveros y Demás",
            "precio": 8.00,
            "descripcion": "Llavero tejido a mano, 100% hipoalergénico.",
            "tipo": "Físico"
        }
    ]

# Encabezado con estilo y toque morado
st.markdown("<h1 style='text-align: center; color: #7209b7;'>🧶 @misgurumii </h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555555; font-size: 18px;'>Amigurumis, tejidos y detalles hechos a mano con mucho amor 💜</p>", unsafe_allow_html=True)

st.divider()

# Menú lateral para elegir vista
menu = st.sidebar.selectbox("Menú de Navegación", ["🛍️ Ver Tienda (Cliente)", "🛠️ Administrar Productos (Tú)"])

# Barra lateral informativa y redes sociales
st.sidebar.divider()
st.sidebar.markdown("### 📱 Mis Redes Sociales")
st.sidebar.markdown("¡Sígueme para ver más creaciones!")
st.sidebar.markdown("🟣 **Instagram:** [@misgurumii](https://instagram.com)")  # Cambia por tu link real
st.sidebar.markdown("🎵 **TikTok:** [@misgurumii](https://tiktok.com)")      # Cambia por tu link real

if menu == "🛍️ Ver Tienda (Cliente)":
    st.header("Catálogo de Productos")
    
    # Filtro por categoría estilizado
    categoria_filtro = st.radio("Filtrar por:", ["Todos", "Tejidos", "Amigurumis, Llaveros y Demás"], horizontal=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Mostrar productos en columnas con diseño de tarjeta
    cols = st.columns(3)
    idx = 0
    
    for prod in st.session_state.productos:
        if categoria_filtro == "Todos" or prod["categoria"] == categoria_filtro:
            with cols[idx % 3]:
                precio_formateado = f"{prod['precio']:.2f}"
                mensaje_whatsapp = f"¡Hola! Me interesa comprar el producto: {prod['nombre']} por ${precio_formateado}"
                whatsapp_link = f"https://wa.me/593900000000?text={mensaje_whatsapp.replace(' ', '%20')}"
                
                # Tarjeta visual en HTML para cada producto
                st.markdown(f"""
                    <div style="background-color: #ffffff; border: 2px solid #e8dff5; border-radius: 12px; padding: 20px; margin-bottom: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                        <h3 style="color: #480ca8; margin-top: 0;">{prod['nombre']}</h3>
                        <p style="color: #6c757d; font-size: 14px; margin-bottom: 5px;"><b>Categoría:</b> {prod['categoria']}</p>
                        <p style="color: #4a4e69; font-size: 18px; font-weight: bold;">${precio_formateado}</p>
                        <p style="color: #333333; font-size: 14px;">{prod['descripcion']}</p>
                        <a href="{whatsapp_link}" target="_blank" style="display: inline-block; background-color: #7209b7; color: white; padding: 8px 15px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 14px; text-align: center; width: 100%;">Comprar por WhatsApp</a>
                    </div>
                """, unsafe_allow_html=True)
            idx += 1

elif menu == "🛠️ Administrar Productos (Tú)":
    st.header("Panel de Administración - Agregar Producto")
    
    with st.form("form_agregar"):
        nombre = st.text_input("Nombre del Producto")
        categoria = st.selectbox("Categoría", ["Tejidos", "Amigurumis, Llaveros y Demás"])
        precio = st.number_input("Precio ($)", min_value=0.0, format="%.2f")
        descripcion = st.text_area("Descripción")
        tipo = st.selectbox("Tipo de producto", ["Físico", "Digital (PDF)"])
        
        submit = st.form_submit_button("Agregar Producto")
        
        if submit:
            if nombre:
                nuevo_prod = {
                    "nombre": nombre,
                    "categoria": categoria,
                    "precio": precio,
                    "descripcion": descripcion,
                    "tipo": tipo
                }
                st.session_state.productos.append(nuevo_prod)
                st.success(f"¡Producto '{nombre}' agregado con éxito!")
            else:
                st.warning("Por favor, ingresa al menos el nombre del producto.")
