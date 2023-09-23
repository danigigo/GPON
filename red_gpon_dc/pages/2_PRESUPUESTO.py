# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:32:07 2023

@author: camac
"""
import streamlit as st

import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Despliegue de RED GPON",
    page_icon="👋",
)

# Definimos los datos

st.write("# :red[PRESUPUESTO DEL DESPLIEGUE]🤑💸🤑")

st.sidebar.success("DANIEL SANTIAGO CAMACHO CALVO ")


# Definimos los datos
data = {
    "Equipos": [
        "Huawei OLT GPON Serie SmartAX EA5800",
        "EA5800 Huawei ONT GPON XGS-PON HG8245A",
        "25 km de fibra optica monomodo",
        "Divisor óptico 1:16 de Anvimur",
        "Divisor óptico 1:32 de Anvimur",
        "Divisor óptico 1:64 de Anvimur",
        " DISTRIBUIDOR INTERNO ÓPTICO BT72 de fukurawa",
        "TOTAL(Se modifica dependiento de cuantas ONTs(routers) se van a usar en cada sede)"
    ],
    "Precio (USD)": ['1200$ x 4', '88$ x 4', '1330$', '12$', '23$', '45$', '850$ x 4','6962$']
}   

# Crear un DataFrame de pandas con los datos
df = pd.DataFrame(data)

# Convertir la columna "Precio (USD)" a texto
df["Precio (USD)"] = df["Precio (USD)"].astype(str)

# Centrar la tabla
st.table(df.style.set_properties(**{'text-align': 'center'}))


# Define el texto
texto = """
La elección de los equipos para el montaje de la red GPON que conecta las sedes de Bucaramanga, Floridablanca, Piedecuesta y Líbano se realizó teniendo en cuenta los siguientes factores:

Topología de anillo: La topología de anillo es la más adecuada para redes GPON, ya que proporciona redundancia y tolerancia a fallos.
Cantidad de usuarios: La cantidad de usuarios en cada sede se determinó en función de los datos demográficos y socioeconómicos de la zona.
Características de los equipos: Los equipos seleccionados son los que mejor se adaptan a las necesidades de la red, en términos de rendimiento, capacidad y características.


"""

# Utiliza st para mostrar el texto con los subtítulos en rojo
st.markdown(texto)
st.markdown('<h3 style="color:red">OLT:</h3>', unsafe_allow_html=True)

# Define el texto para OLT
texto_olt = """
**Huawei OLT GPON Serie SmartAX EA5800:** Esta serie de OLTs ofrece un rendimiento y una escalabilidad excepcionales para redes de fibra óptica. Es la opción ideal para redes con una gran cantidad de usuarios.

* Razones para elegir los OLTs Huawei OLT GPON Serie SmartAX EA5800:
  - Soporte de tecnologías GPON, XG-PON y XGS-PON
  - Hasta 8 puertos GPON, 4 puertos XG-PON y 12 puertos GE/FE
  - Capacidad de conmutación de hasta 800 Gbps
  - Capacidad de reenvío de paquetes de hasta 100 Mpps
  - Soporte de hasta 16.384 ONTs por puerto GPON y hasta 8.192 ONTs por puerto XGS-PON
  - Soporte de IPv4, IPv6, VLAN, QoS y ACL
"""

# Utiliza st para mostrar el texto de OLT en rojo
st.markdown(texto_olt, unsafe_allow_html=True)

# Define el texto para ONT
st.markdown('<h3 style="color:red">ONT:</h3>', unsafe_allow_html=True)

texto_ont = """
**Huawei ONT GPON XGS-PON HG8245A:** Esta ONT ofrece un rendimiento y una funcionalidad excepcionales para usuarios residenciales y empresariales. Es la opción ideal para redes GPON con una gran cantidad de usuarios.

* Razones para elegir las ONTs Huawei ONT GPON XGS-PON HG8245A:
  - Soporte de tecnologías GPON y XGS-PON
  - 4 puertos Gigabit Ethernet
  - 1 puerto POTS
  - Soporte de IPv4, IPv6, VLAN, QoS y ACL
  - Soporte de Wi-Fi 6
  - Soporte de tecnología Mesh Wi-Fi
  - Soporte de tecnología IPTV
  - Soporte de tecnología VoIP
"""

# Utiliza st para mostrar el texto de ONT en rojo
st.markdown(texto_ont, unsafe_allow_html=True)

# Define el texto para Fibra óptica
st.markdown('<h3 style="color:red">FIBRA OPTICA:</h3>', unsafe_allow_html=True)

texto_fibra = """
**Fibra óptica monomodo 10G:** Esta fibra óptica ofrece un rendimiento excepcional para redes GPON. Es la opción ideal para redes con una gran cantidad de usuarios.

* Razones para elegir la fibra óptica monomodo 10G:
  - Capacidad de transmisión de hasta 10 Gbps
  - Distancia de transmisión de hasta 100 km
  - Resistencia a la atenuación
  - Resistencia a la corrosión
"""

# Utiliza st para mostrar el texto de Fibra óptica en rojo
st.markdown(texto_fibra, unsafe_allow_html=True)
st.markdown('<h3 style="color:red">DIVISORES OPTICOS:</h3>', unsafe_allow_html=True)
st.markdown("""<p style='text-align: justify;'>En las diferentes sedes universitarias, es necesario proporcionar una gran cantidad de ancho de banda para satisfacer las necesidades de los usuarios. Por lo tanto, las sedes universitarias grandes suelen utilizar divisores ópticos con una relación de división menor, como 1:16 o 1:32. Y en la del limonal que es más pequeña se usan los de 1:64(para logar reducir gastos ya que no habrá tanta demanda pues no hay tantas personas).""",unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
image8 = Image.open('xdd.jpg')
st.image(image8)