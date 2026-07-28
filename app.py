import streamlit as st

# Configuración de la página
st.set_page_config(page_title="@misgurumii - Tienda", page_icon="🧶", layout="wide")

# "Base de datos" temporal en memoria (simulada con la sesión de Streamlit)
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

# Título principal
st.title("🧶 @misgurumii - Tienda Oficial")

# Menú lateral para elegir entre ver la tienda o administrar
menu = st.sidebar.selectbox("Menú de Navegación", ["🛍️ Ver Tienda (Cliente)", "🛠️ Administrar Productos (Tú)"])

if menu == "🛍️ Ver Tienda (Cliente)":
    st.header("Catálogo de Productos")
    
    # Filtro por categoría
    categoria_filtro = st.radio("Filtrar por:", ["Todos", "Tejidos", "Amigurumis, Llaveros y Demás"], horizontal=True)
    
    st.divider()
    
    # Mostrar productos en columnas
    cols = st.columns(3)
    idx = 0
    
    for prod in st.session_state.productos:
        if categoria_filtro == "Todos" or prod["categoria"] == categoria_filtro:
            with cols[idx % 3]:
                st.subheader(prod["nombre"])
                st.write(f"**Categoría:** {prod['categoria']}")
...                 st.write(f"**Precio:** ${prod['precio']:.2f}")
...                 st.write(prod["descripcion"])
...                 
...                 # Botón de compra directa a WhatsApp (puedes cambiar tu número)
...                 mensaje_whatsapp = f"¡Hola! Me interesa comprar el producto: {prod['nombre']} por ${prod['precio']:.2f}"
...                 whatsapp_link = f"https://wa.me/593900000000?text={mensaje_whatsapp.replace(' ', '%20')}"
...                 
...                 st.markdown(f"[Comprar por WhatsApp]({whatsapp_link})")
...                 st.divider()
...             idx += 1
... 
... elif menu == "🛠️ Administrar Productos (Tú)":
...     st.header("Panel de Administración - Agregar Producto")
...     
...     with st.form("form_agregar"):
...         nombre = st.text_input("Nombre del Producto")
...         categoria = st.selectbox("Categoría", ["Tejidos", "Amigurumis, Llaveros y Demás"])
...         precio = st.number_input("Precio ($)", min_value=0.0, format="%.2f")
...         descripcion = st.text_area("Descripción")
...         tipo = st.selectbox("Tipo de producto", ["Físico", "Digital (PDF)"])
...         
...         submit = st.form_submit_button("Agregar Producto")
...         
...         if submit:
...             if nombre:
...                 nuevo_prod = {
...                     "nombre": nombre,
...                     "categoria": categoria,
...                     "precio": precio,
...                     "descripcion": descripcion,
...                     "tipo": tipo
...                 }
...                 st.session_state.productos.append(nuevo_prod)
...                 st.success(f"¡Producto '{nombre}' agregado con éxito!")
...             else:
