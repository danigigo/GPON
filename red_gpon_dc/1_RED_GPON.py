# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:11:33 2023

@author: camac
"""

import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Despliegue de RED GPON",
    page_icon="👋",
)

st.write("# :red[¿QUE ES UNA RED GPON?]💻📡🖥️ ")

st.sidebar.success("DANIEL SANTIAGO CAMACHO CALVO ")

st.markdown("""<p style='text-align: justify;'>Una Gigabit Passive Optical Network o GPON por
            sus siglas es un tipo de red  pasiva de fibra óptica que se utiliza principalmente para la
            transmisión de datos en aplicaciones de telecomunicaciones, esta puede llegar a 
            una capacidad de tráfico de hasta 2,5 Gbps en downstream (bajada) y 1,25 Gbps en 
            sentido upstream (subida), lo que hace que proporcione estabilidad y escalabilidad 
            para conexiones de banda ancha.<br></br> Una red óptica pasiva ( PON) permite eliminar todos los componentes activos existentes entre el servidor y el
            cliente introduciendo en su lugar componentes ópticos pasivos (divisores ópticos pasivos) para guiar 
            el tráfico por la red, cuyo elemento principal es el dispositivo divisor óptico (conocido como splitter).
            La utilización de estos sistemas pasivos reduce considerablemente los costes y son utilizados en las redes
            FTTH.</p>""",unsafe_allow_html=True)

# :red[""]


image = Image.open('hhhh.JPG')

st.image(image)



st.write("# :blue[CARACTERISTICAS DE UNA RED GPON]📲🛰️📺")

caracteristicas = [
    "🌐 Ancho de banda contando con velocidades de descarga y carga asimétricas:",
    "Las redes GPON ofrecen un ancho de banda de hasta 2,5 Gbps en sentido descendente y 1,25 Gbps en sentido ascendente",
    "🌐 Distancia:",
    " La distancia máxima entre la OLT y la ONT es de 20 km.",
    "🌐 Eficiencia:",
    " Las redes GPON tienen una eficiencia de hasta el 93%.",
    "🌐 División pasiva: ",
    "Se refiere a que se usa división pasiva de la señal de fibra óptica en múltiples conexiones para llegar a varios usuarios.",
    "🌐 Multiplexación por división de tiempo (TDM):",
    " Para asignar el ancho de banda a diferentes usuarios. Esto significa que la red puede compartir eficientemente la capacidad entre múltiples usuarios sin interferencias.",
    "🌐 Capacidad de ancho de banda escalable: ",
    "Se puede aumentar la capacidad de la red según sea necesario para satisfacer la demanda de los usuarios."
]

for caracteristica in caracteristicas:
    if caracteristica.startswith("🌐"):
        st.markdown(f'<span style="color:red">{caracteristica}</span>', unsafe_allow_html=True)
    else:
        st.markdown(caracteristica)

image2 = Image.open('ffd.JPG')

st.image(image2)
