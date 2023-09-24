# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:32:07 2023

@author: camac
"""

import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Despliegue de RED GPON",
    page_icon="👋",
)

st.write("# :red[ELEMENTOS DE UNA RED GPON]💾 ")

st.sidebar.success("DANIEL SANTIAGO CAMACHO CALVO ")




# OLT (Optical Line Terminal)
st.markdown('<h3 style="color:green">OLT (Optical Line Terminal):</h3>', unsafe_allow_html=True)
st.write("El OLT es el punto de inicio de la red GPON y se encuentra en la central del proveedor de servicios. "
         "Es responsable de gestionar y controlar toda la red GPON, así como de convertir los datos eléctricos en señales ópticas para transmitirlos a través de la red de fibra óptica.")

image3 = Image.open('olt.jpeg')
st.image(image3)

# ONT/ONU (Optical Network Terminal/Optical Network Unit)
st.markdown('<h3 style="color:green">ONT/ONU (Optical Network Terminal/Optical Network Unit):</h3>', unsafe_allow_html=True)
st.write("La ONT o ONU es el dispositivo que se instala en la ubicación del usuario final, como un hogar o una empresa. "
         "Es responsable de convertir las señales ópticas en señales eléctricas que los dispositivos del usuario final pueden utilizar, como computadoras, teléfonos o televisores.")

image4 = Image.open('onu.jpg')
st.image(image4)

st.markdown('<h3 style="color:green">DISTRIBUIDOR INTERNO OPTICO (DIO) ):</h3>', unsafe_allow_html=True)
st.write("Se utiliza para conectar cables y cordones ópticos en una red de fibra óptica. Los DIO se utilizan para distribuir la señal óptica desde un cable principal a cables o cordones más pequeños que se conectan a los equipos de red, como los OLT y las ONT.")

image9 = Image.open('dio.png')
st.image(image9)


# ODN (Optical Distribution Network)
st.markdown('<h3 style="color:green">ODN (Optical Distribution Network):</h3>', unsafe_allow_html=True)
st.write("El ODN se refiere a la red de fibra óptica que conecta la OLT con las ONT. Incluye cables de fibra óptica, "
         "empalmes, splitters y otros componentes pasivos que distribuyen la señal óptica somo lo son: ")


caracteristicas = [
    "Fibra óptica: El medio de transmisión usado, utilizando luz",
    "Empalmes: Son dispositivos que se utilizan para conectar dos cables de fibra óptica. Los empalmes pueden ser de varios tipos, pero los más comunes son los empalmes mecánicos y los empalmes fusionados.",
    "Divisores ópticos (splitters): Son dispositivos pasivos que dividen la señal óptica de la OLT en múltiples señales para las ONT.",
    "Otros componentes pasivos: Pueden incluir atenuadores, amplificadores y filtros."
]

formatted_caracteristicas = []

for caracteristica in caracteristicas:
    parts = caracteristica.split(":")
    if len(parts) == 2:
        formatted_caracteristica = f'<span style="color:red">{parts[0]}:</span> {parts[1]}'
    else:
        formatted_caracteristica = caracteristica
    formatted_caracteristicas.append(formatted_caracteristica)

st.markdown("\n\n".join(formatted_caracteristicas), unsafe_allow_html=True)

image5 = Image.open('ond.png')
st.image(image5)




            
st.write("# :blue[EQUIPOS A USAR EN ESTA RED]🎯🖥️")


# Crear una lista de diccionarios con la información de las sedes y equipos
sedes_equipos = [
    {
        'Sede': 'Sedes Bucaramanga y Floridablanca',
        'OLT': 'Huawei OLT GPON Serie SmartAX EA5800',
        'ONT': 'Huawei ONT GPON XGS-PON HG8245A',
        'Fibra': 'Fibra óptica monomodo 10G',
        'DIO': 'DISTRIBUIDOR INTERNO ÓPTICO BT72 de fukurawa',
        'Divisores ópticos': 'Divisores ópticos 1:16'
    },
    {
        'Sede': 'Sede Piedecuesta',
        'OLT': 'Huawei OLT GPON Serie SmartAX EA5800',
        'ONT': 'Huawei ONT GPON XGS-PON HG8245A',
        'Fibra': 'Fibra óptica monomodo 10G',
        'DIO': 'DISTRIBUIDOR INTERNO ÓPTICO BT72 de fukurawa',
        'Divisores ópticos': 'Divisores ópticos 1:32'
    },
    {
        'Sede': 'Sede Limonal',
        'OLT': 'Huawei OLT GPON Serie SmartAX EA5800',
        'ONT': 'Huawei ONT GPON XGS-PON HG8245A',
        'Fibra': 'Fibra óptica monomodo 10G',
        'DIO': 'DISTRIBUIDOR INTERNO ÓPTICO BT72 de fukurawa',
        'Divisores ópticos': 'Divisores ópticos 1:64'
    }
]


st.table(sedes_equipos)
  

# Lista de equipos con sus enlaces a las data sheets
equipos = [
    ("Huawei OLT GPON Serie SmartAX EA5800", "https://www.router-switch.com/media/upload/product-pdf/huawei-smartax-ea5800-datasheet.pdf"),
    ("Huawei ONT GPON XGS-PON HG8245A", "https://www.router-switch.com/pdf2html/pdf/hg8245a-datasheet.pdf"),
    ("Divisor óptico 1:16 de Anvimur", "https://www.anvimur.com/es/material-fibra-optica/1783-splitter-116-colores-conector-scapc.html"),
    ("Divisor óptico 1:32 de Anvimur", "https://www.anvimur.com/es/material-fibra-optica/1784-splitter-132-colores-conector-scapc.html"),
    ("Divisor óptico 1:64 de Anvimur", "https://www.anvimur.com/es/material-fibra-optica/1785-splitter-164-caja-scapc.html"),
    ("DISTRIBUIDOR INTERNO ÓPTICO BT72 de fukurawa", "https://www.furukawalatam.com/es/catalogo-de-productos-detalles/distribuidor-interno-optico-bt72"),
]

# Título de la aplicación
st.write("# :green[Datasheets de equipos usados]🖥️")

# Bucle para mostrar cada equipo con su enlace a la data sheet
for equipo in equipos:
    # Texto del botón
    button_text = equipo[0] + " - Datasheet"

    # Enlace al archivo de la data sheet
    link = equipo[1]

    # Botón con enlace a la data sheet
    st.markdown(f"""
    <a href="{link}" target="_blank">{button_text}</a>
    """, unsafe_allow_html=True)
  
    
st.write("# :blue[ESPECIFICACIONES TECNICAS]⌨️🌐")



# Estilo CSS para los subtítulos
titulo_css = """
    <style>
        .titulo {
            color: red;
            font-size: 24px;
        }
    </style>
"""

# Especificaciones técnicas del OLT Huawei HG8560A
st.markdown(titulo_css, unsafe_allow_html=True)
st.write('<span class="titulo">Especificaciones Técnicas del OLT Serie SmartAX EA5800:</span>', unsafe_allow_html=True)

# Caracterísiticas
st.markdown("""
**Características:**

* **Tecnología:** GPON, XG-PON, XGS-PON, GE y 10GE
* **Modos de construcción de red:** POL, FTTH, FTTB y FTTC
* **Capacidad:** Hasta 12,8 Tbps
* **Puertos:** 16, 32, 48 o 64 puertos PON
* **Funciones:** QoS, seguridad, gestión remota
* **Eficiencia energética:** 802.3az
""")

# Datos
data = {
    "Tecnología": "GPON, XG-PON, XGS-PON, GE y 10GE",
    "Modos de construcción de red": "POL, FTTH, FTTB y FTTC",
    "Capacidad": "Hasta 12,8 Tbps",
    "Puertos": "16, 32, 48 o 64 puertos PON",
    "Funciones": "QoS, seguridad, gestión remota",
    "Eficiencia energética": "802.3az",
}

# Tabla
st.table(data)


image6 = Image.open('hud.png')
st.image(image6)  
# Espacio en blanco entre las especificaciones de los equipos
st.write("")

# Especificaciones técnicas del ONT Huawei HG8245A
st.markdown(titulo_css, unsafe_allow_html=True)
st.write('<span class="titulo">Especificaciones Técnicas del ONT Huawei HG8245A:</span>', unsafe_allow_html=True)

st.markdown("""
**Características:**

* **Puerto GPON:** Clase B+
* **Puertos Ethernet:** 4 Gigabit Ethernet (LAN)
* **Puertos POTS:** 2 puertos telefónicos
* **Capacidad de red inalámbrica:** IEEE 802.11 b/g/n
* **Puerto USB:** USB 2.0
* **Funciones de Capa 3:** QoS, seguridad, energía
* **Eficiencia energética:** 802.3az
""")

# Datos
data = {
    "Puerto GPON": "Clase B+",
    "Puertos Ethernet": "4 Gigabit Ethernet (LAN)",
    "Puertos POTS": "2 puertos telefónicos",
    "Capacidad de red inalámbrica": "IEEE 802.11 b/g/n",
    "Puerto USB": "USB 2.0",
    "Funciones de Capa 3": "QoS, seguridad, energía",
    "Eficiencia energética": "802.3az",
}

# Tabla
st.table(data)


image7 = Image.open('raw.jpg')
st.image(image7)


st.markdown(titulo_css, unsafe_allow_html=True)
st.write('<span class="titulo">Especificaciones Técnicas del DISTRIBUIDOR INTERNO ÓPTICO BT72 de fukurawa</span>', unsafe_allow_html=True)

st.markdown("""
**Características:**

* **Capacidad:** Hasta 72 empalmes
* **Dimensiones:** 482 x 220 x 45 mm (ancho x alto x profundidad)
* **Peso:** 2,5 kg
* **Material:** Plástico de alto impacto
* **Tipo:** Pasivo
* **Montaje:** Rack
* **Longitudes de onda compatibles:** 1310 nm y 1490 nm
* **Soporta cables y cordones ópticos de:** 2,0 a 9,0 mm
""")

# Datos
data = {
    "Capacidad": "Hasta 72 empalmes",
    "Dimensiones": "482 x 220 x 45 mm (ancho x alto x profundidad)",
    "Peso": "2,5 kg",
    "Material": "Plástico de alto impacto",
    "Tipo": "Pasivo",
    "Montaje": "Rack",
    "Longitudes de onda compatibles": "1310 nm y 1490 nm",
    "Soporta cables y cordones ópticos de": "2,0 a 9,0 mm",
}

# Tabla
st.table(data)

image99 = Image.open('dio.png')
st.image(image99)

     

# Título de la aplicación
st.write("# :red[Divisores opticos Avimur:]")


# Lista de imágenes y descripciones
imagenes = ["1_16.jpg", "1_32.jpg", "1_64.jpg"]
descripciones = ["Divisor óptico 1:16", "Divisor óptico 1:32", "Divisor óptico 1:64"]

# Crea tres columnas para mostrar las imágenes y descripciones
col1, col2, col3 = st.columns(3)

# Columna 1 - Imagen 1
with col1:
    st.image(imagenes[0], use_column_width=True)
    st.write(descripciones[0])

# Columna 2 - Imagen 2
with col2:
    st.image(imagenes[1], use_column_width=True)
    st.write(descripciones[1])

# Columna 3 - Imagen 3
with col3:
    st.image(imagenes[2], use_column_width=True)
    st.write(descripciones[2])




# Caracterísiticas
st.markdown("""
**Características:**

* **Marca:** Avimur
* **Modelos:** 1:16, 1:32 y 1:64
* **Tecnología:** GPON
* **Pérdidas por división:** 3 dB
* **Pérdidas de insercción:** 0,3 dB
* **Material:** Plástico de alto impacto
* **Dimensiones:** 482 x 220 x 45 mm (ancho x alto x profundidad)
* **Peso:** 2,5 kg
* **Montaje:** Rack

**Características específicas:**

* **Divisor óptico 1:16:** 16 salidas
* **Divisor óptico 1:32:** 32 salidas
* **Divisor óptico 1:64:** 64 salidas

**Funciones:**

* **Dividir la señal óptica de una fibra principal en varias fibras secundarias**
* **Utilizado en redes PON**
* **Compatible con la mayoría de los equipos de red**
""")

# Tabla
st.table(data)




