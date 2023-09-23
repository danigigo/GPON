# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:32:07 2023

@author: camac
"""
import folium
import streamlit as st
from streamlit_folium import st_folium




st.set_page_config(
    page_title="Despliegue de RED GPON",
    page_icon="👋",
)




st.write("# :red[MAPA DE DESPLIEGUE]🚀🚀🚀 ")

st.sidebar.success("DANIEL SANTIAGO CAMACHO CALVO ")

st.markdown("""<p style='text-align: justify;'>Esta es el mapa de el despliegue de la red GPON en las 4 sedes de la universidad donde se puede observar las ubicaciones de las mismas y de los equipos claves de la red, tambien se puede observar las celdas  de coberturaen las cedes<br></br></p>""",unsafe_allow_html=True)

            

# Crear un mapa de Folium
m = folium.Map(location=[7.137061040191279, -73.12805527231112], zoom_start=14)

# Definir información de las sedes
locations = [
    {
        'name': 'Sede Bucaramanga',
        'lat': 7.137061040191279,
        'lon': -73.12805527231112,
        'description': 'OLT:SmartAX EA5800, DIO: BT72 de fukurawa  y ONTs:GPON XGS-PON HG8245A(donde se neseciten)'
    },
    {
        'name': 'Sede Floridablanca',
        'lat': 7.065556432696987,
        'lon': -73.09531850115162,
        'description': 'OLT:SmartAX EA5800, DIO: BT72 de fukurawa  y ONTs:GPON XGS-PON HG8245A(donde se neseciten)'
    },
    {
        'name': 'Sede Piedecuesta',
        'lat': 7.022842715565784,
        'lon': -73.05940429202747,
        'description': 'OLT:SmartAX EA5800, DIO: BT72 de fukurawa y ONTs:GPON XGS-PON HG8245A(donde se neseciten)'
    },
    {
        'name': 'Sede Limonal',
        'lat': 7.008073410481673,
        'lon': -73.05142322999137,
        'description': 'OLT:SmartAX EA5800, DIO: BT72 de fukurawa Y ONTs:GPON XGS-PON HG8245A(donde se neseciten)'
    },
    {
        'name': 'OLT',
        'lat': 7.136840099821886,
        'lon': -73.12826831383893,  
        'description': 'SmartAX EA5800'
    },
    {
        'name': 'OLT',
        'lat': 7.0659331755991035,
        'lon': -73.09515162654911,   
        'description': 'SmartAX EA5800'
    },
    {
        'name': 'OLT',
        'lat': 7.023197115545892,
        'lon': -73.059312702016,
        'description': 'SmartAX EA5800'
    },
    {
        'name': 'OLT',
        'lat': 7.008130431591074,
        'lon': -73.05142290404254, 
        'description': 'SmartAX EA5800'
    },
    {
        'name': 'Splitter y DIO',
        'lat': 7.136883660667875,
        'lon': -73.12824163431057,   
        'description': '1:16 y BT72'
    },
    {
        'name': 'Splitter y DIO',
        'lat': 7.066081439952267,
        'lon': -73.09521195684997,   
        'description': '1:16 y BT72'
    },
    {
        'name': 'Splitter y DIO',
        'lat': 7.008073410481673,
        'lon': -73.05142322999137, 
        'description': '1:32 y BT72'
    },
    {
        'name': 'Splitter y DIO',
        'lat': 7.023233889480684,
        'lon': -73.05919685098638,  
        'description': '1:64 y BT72'
    },
    { 
        'name': 'ISP (proveedor)',
        'lat': 7.1057876425763915,
        'lon': -73.11560920930712,
        'description': 'Instlaciones del proveedor de servicio(en este caso)'
    }
]




# Agregar marcadores con información personalizada
for location in locations:
    folium.Marker(
        location=[location['lat'], location['lon']],
        icon=folium.Icon(color='purple'),
        popup=folium.Popup(location['description'], max_width=300),  # Descripción personalizada
        tooltip=location['name']
    ).add_to(m)

# Agregar hexágono para la celda de cobertura de red óptica
folium.RegularPolygonMarker(
    location=[7.136844296154591, -73.12832180456587],  # Ubicación de la sede Bucaramanga
    fill_color='red',
    fill_opacity=0.5,
    number_of_sides=6,  # Hexágono
    radius=100,  # Radio del hexágono en metros
    
    tooltip='Celda Cobertura Sede Bucaramanga'
).add_to(m)



folium.RegularPolygonMarker(
    location=[7.066195857926469, -73.09492035409652],  # Ubicación de la sede Bucaramanga
    fill_color='red',
    fill_opacity=0.5,
    number_of_sides=6,  # Hexágono
    radius=190,  # Radio del hexágono en metros
    
    tooltip='Celda Cobertura Sede Floridablanca'

).add_to(m)
folium.RegularPolygonMarker(
    location=[7.023262911646313, -73.05971245467781],  # Ubicación de la sede Bucaramanga
    fill_color='red',
    fill_opacity=0.5,
    number_of_sides=6,  # Hexágono
    radius=233,  # Radio del hexágono en metros
    
    tooltip='Celda Cobertura Sede Piedecuesta'
).add_to(m)
folium.RegularPolygonMarker(
    location=[7.0084293135346725, -73.05136176052113],  # Ubicación de la sede Bucaramanga
    fill_color='red',
    fill_opacity=0.5,
    number_of_sides=6,  # Hexágono
    radius=155,  # Radio del hexágono en metros
    
    tooltip='Celda Cobertura Sede Limonal'
).add_to(m)
# Llamar a la función para renderizar el mapa de Folium en Streamlit
st_data = st_folium(m, width=1000)


