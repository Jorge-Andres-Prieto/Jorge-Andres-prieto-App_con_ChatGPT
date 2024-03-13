import streamlit as st

# Función para el inicio de sesión
def login():
  st.title("Inicio de Sesión")
  usuario = st.text_input("Usuario")
  contraseña = st.text_input("Contraseña", type="password")
  iniciar_sesion = st.button("Iniciar Sesión")

  if iniciar_sesion:
    if usuario == "123" and contraseña == "123":
      st.session_state.logged_in = True
      st.experimental_rerun()
    else:
      st.error("Usuario o contraseña incorrectos")

# Función para el menú principal
def menu():
  st.sidebar.title("Menú")
  opciones = [
    "Conversiones de Temperatura",
    "Conversiones de Longitud",
    "Conversiones de Peso/Masa",
    "Conversiones de Volumen",
    "Conversiones de Tiempo",
    "Conversiones de Velocidad",
    "Conversiones de Área",
    "Conversiones de Energía",
    "Conversiones de Presión",
    "Conversiones de Tamaño de Datos"
  ]
  seleccion = st.sidebar.radio("Seleccione una categoría", opciones)

  if seleccion == "Conversiones de Temperatura":
    temperatura()
  elif seleccion == "Conversiones de Longitud":
    longitud()
  elif seleccion == "Conversiones de Peso/Masa":
    peso_masa()
  elif seleccion == "Conversiones de Volumen":
    volumen()
  elif seleccion == "Conversiones de Tiempo":
    tiempo()
  elif seleccion == "Conversiones de Velocidad":
    velocidad()
  elif seleccion == "Conversiones de Área":
    area()
  elif seleccion == "Conversiones de Energía":
    energia()
  elif seleccion == "Conversiones de Presión":
    presion()
  elif seleccion == "Conversiones de Tamaño de Datos":
    tamanio_datos()

# Función para las conversiones de temperatura
def temperatura():
  st.title("Conversiones de Temperatura")
  opciones = ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"]
  conversion = st.selectbox("Seleccione el tipo de conversión", opciones)
  valor = st.number_input("Ingrese el valor a convertir")

  if conversion == "Celsius a Fahrenheit":
    resultado = valor * 9/5 + 32
    st.write(f"{valor}°C equivalen a {resultado:.2f}°F")
  elif conversion == "Fahrenheit a Celsius":
    resultado = (valor - 32) * 5/9
    st.write(f"{valor}°F equivalen a {resultado:.2f}°C")
  elif conversion == "Celsius a Kelvin":
    resultado = valor + 273.15
    st.write(f"{valor}°C equivalen a {resultado:.2f}K")
  elif conversion == "Kelvin a Celsius":
    resultado = valor - 273.15
    st.write(f"{valor}K equivalen a {resultado:.2f}°C")

# Función para las conversiones de longitud
def longitud():
  st.title("Conversiones de Longitud")
  opciones = ["Metros a Pies", "Pies a Metros", "Centímetros a Pulgadas", "Pulgadas a Centímetros"]
  conversion = st.selectbox("Seleccione el tipo de conversión", opciones)
  valor = st.number_input("Ingrese el valor a convertir")

  if conversion == "Metros a Pies":
    resultado = valor * 3.28084
    st.write(f"{valor}m equivalen a {resultado:.2f}ft")
  elif conversion == "Pies a Metros":
    resultado = valor / 3.28084
    st.write(f"{valor}ft equivalen a {resultado:.2f}m")
  elif conversion == "Centímetros a Pulgadas":
    resultado = valor * 0.393701
    st.write(f"{valor}cm equivalen a {resultado:.2f}in")
  elif conversion == "Pulgadas a Centímetros":
    resultado = valor / 0.393701
    st.write(f"{valor}in equivalen a {resultado:.2f}cm")
    # Función para las conversiones de peso/masa
def peso_masa():
  st.title("Conversiones de Peso/Masa")
  opciones = ["Kilogramos a Libras", "Libras a Kilogramos", "Gramos a Onzas", "Onzas a Gramos"]
  conversion = st.selectbox("Seleccione el tipo de conversión", opciones)
  valor = st.number_input("Ingrese el valor a convertir")

  if conversion == "Kilogramos a Libras":
    resultado = valor * 2.20462
    st.write(f"{valor}kg equivalen a {resultado:.2f}lb")
  elif conversion == "Libras a Kilogramos":
    resultado = valor / 2.20462
    st.write(f"{valor}lb equivalen a {resultado:.2f}kg")
  elif conversion == "Gramos a Onzas":
    resultado = valor * 0.035274
    st.write(f"{valor}g equivalen a {resultado:.2f}oz")
  elif conversion == "Onzas a Gramos":
    resultado = valor / 0.035274
    st.write(f"{valor}oz equivalen a {resultado:.2f}g")

# Función para las conversiones de volumen
def volumen():
  st.title("Conversiones de Volumen")
  opciones = ["Litros a Galones", "Galones a Litros", "Mililitros a Onzas líquidas", "Onzas líquidas a Mililitros"]
  conversion = st.selectbox("Seleccione el tipo de conversión", opciones)
  valor = st.number_input("Ingrese el valor a convertir")

  if conversion == "Litros a Galones":
    resultado = valor * 0.264172
    st.write(f"{valor}L equivalen a {resultado:.2f}gal")
  elif conversion == "Galones a Litros":
    resultado = valor / 0.264172
    st.write(f"{valor}gal equivalen a {resultado:.2f}L")
  elif conversion == "Mililitros a Onzas líquidas":
    resultado = valor * 0.033814
    st.write(f"{valor}ml equivalen a {resultado:.2f}fl oz")
  elif conversion == "Onzas líquidas a Mililitros":
    resultado = valor / 0.033814
    st.write(f"{valor}fl oz equivalen a {resultado:.2f}ml")

# Función para las conversiones de tiempo
def tiempo():
  st.title("Conversiones de Tiempo")
  opciones = ["Segundos a Horas", "Horas a Segundos", "Minutos a Segundos", "Segundos a Minutos"]
  conversion = st.selectbox("Seleccione el tipo de conversión", opciones)
  valor = st.number_input("Ingrese el valor a convertir")

  if conversion == "Segundos a Horas":
    resultado = valor / 3600
    st.write(f"{valor}s equivalen a {resultado:.2f}h")
  elif conversion == "Horas a Segundos":
    resultado = valor * 3600
    st.write(f"{valor}h equivalen a {resultado:.2f}s")
  elif conversion == "Minutos a Segundos":
    resultado = valor * 60
    st.write(f"{valor}min equivalen a {resultado:.2f}s")
  elif conversion == "Segundos a Minutos":
    resultado = valor / 60
    st.write(f"{valor}s equivalen a {resultado:.2f}min")

# Función para las conversiones de velocidad
def velocidad():
  st.title("Conversiones de Velocidad")
  opciones = ["Kilómetros por hora a Millas por hora", "Millas por hora a Kilómetros por hora", "Metros por segundo a Pies por segundo", "Pies por segundo a Metros por segundo"]
  conversion = st.selectbox("Seleccione el tipo de conversión", opciones)
  valor = st.number_input("Ingrese el valor a convertir")

  if conversion == "Kilómetros por hora a Millas por hora":
    resultado = valor * 0.621371
    st.write(f"{valor}km/h equivalen a {resultado:.2f}mph")
  elif conversion == "Millas por hora a Kilómetros por hora":
    resultado = valor * 1.60934
    st.write(f"{valor}mph equivalen a {resultado:.2f}km/h")
  elif conversion == "Metros por segundo a Pies por segundo":
    resultado = valor * 3.28084
    st.write(f"{valor}m/s equivalen a {resultado:.2f}ft/s")
  elif conversion == "Pies por segundo a Metros por segundo":
    resultado = valor / 3.28084
    st.write(f"{valor}ft/s equivalen a {resultado:.2f}m/s")

# Función para las conversiones de área
def area():
  st.title("Conversiones de Área")
  opciones = ["Metros cuadrados a Pies cuadrados", "Pies cuadrados a Metros cuadrados", "Centímetros cuadrados a Pulgadas cuadradas", "Pulgadas cuadradas a Centímetros cuadrados"]
  conversion = st.selectbox("Seleccione el tipo de conversión", opciones)
  valor = st.number_input("Ingrese el valor a convertir")

  if conversion == "Metros cuadrados a Pies cuadrados":
    resultado = valor * 10.7639
    st.write(f"{valor}m² equivalen a {resultado:.2f}ft²")
  elif conversion == "Pies cuadrados a Metros cuadrados":
    resultado = valor / 10.7639
    st.write(f"{valor}ft² equivalen a {resultado:.2f}m²")
  elif conversion == "Centímetros cuadrados a Pulgadas cuadradas":
    resultado = valor * 0.155000
    st.write(f"{valor}cm² equivalen a {resultado:.2f}in²")
  elif conversion == "Pulgadas cuadradas a Centímetros cuadrados":
    resultado = valor / 0.155000
    st.write(f"{valor}in² equivalen a {resultado:.2f}cm²")

# Función para las conversiones de energía
def energia():
  st.title("Conversiones de Energía")
  opciones = ["Julios a Joules", "Joules a Julios", "Kilojulios a Kilocalorías", "Kilocalorías a Kilojulios", "Vatios-hora a Kilovatios-hora", "Kilovatios-hora a Vatios-hora"]
  conversion = st.selectbox("Seleccione el tipo de conversión", opciones)
  valor = st.number_input("Ingrese el valor a convertir")

  if conversion == "Julios a Joules":
    resultado = valor
    st.write(f"{valor}J equivalen a {resultado:.2f}J")
  elif conversion == "Joules a Julios":
    resultado = valor
    st.write(f"{valor}J equivalen a {resultado:.2f}J")
  elif conversion == "Kilojulios a Kilocalorías":
    resultado = valor * 0.239006
    st.write(f"{valor}kJ equivalen a {resultado:.2f}kcal")
  elif conversion == "Kilocalorías a Kilojulios":
    resultado = valor * 4.184
    st.write(f"{valor}kcal equivalen a {resultado:.2f}kJ")
  elif conversion == "Vatios-hora a Kilovatios-hora":
    resultado = valor / 1000
    st.write(f"{valor}Wh equivalen a {resultado:.2f}kWh")
  elif conversion == "Kilovatios-hora a Vatios-hora":
    resultado = valor * 1000
    st.write(f"{valor}kWh equivalen a {resultado:.2f}Wh")

# Función para las conversiones de presión
def presion():
  st.title("Conversiones de Presión")
  opciones = ["Pascales a Pa", "Pa a Pascales", "Pascales a Bar", "Bar a Pascales", "Pascales a Atmosferas", "Atmosferas a Pascales"]
  conversion = st.selectbox("Seleccione el tipo de conversión", opciones)
  valor = st.number_input("Ingrese el valor a convertir")

  if conversion == "Pascales a Pa":
    resultado = valor
    st.write(f"{valor}Pa equivalen a {resultado:.2f}Pa")
  elif conversion == "Pa a Pascales":
    resultado = valor
    st.write(f"{valor}Pa equivalen a {resultado:.2f}Pa")
  elif conversion == "Pascales a Bar":
    resultado = valor / 100000
    st.write(f"{valor}Pa equivalen a {resultado:.2f}bar")
  elif conversion == "Bar a Pascales":
    resultado = valor * 100000
    st.write(f"{valor}bar equivalen a {resultado:.2f}Pa")
  elif conversion == "Pascales a Atmosferas":
    resultado = valor / 101325
    st.write(f"{valor}Pa equivalen a {resultado:.2f}atm")
  elif conversion == "Atmosferas a Pascales":
    resultado = valor * 101325
    st.write(f"{valor}atm equivalen a {resultado:.2f}Pa")

# Función para las conversiones de tamaño de datos
def tamanio_datos():
  st.title("Conversiones de Tamaño de Datos")
  opciones = ["Bytes a Kilobytes", "Kilobytes a Bytes", "Megabytes a Gigabytes", "Gigabytes a Megabytes", "Terabytes a Petabytes", "Petabytes a Terabytes"]
  conversion = st.selectbox("Seleccione el tipo de conversión", opciones)
  valor = st.number_input("Ingrese el valor a convertir")

  if conversion == "Bytes a Kilobytes":
    resultado = valor / 1024
    st.write(f"{valor}B equivalen a {resultado:.2f}KB")
  elif conversion == "Kilobytes a Bytes":
    resultado = valor * 1024
    st.write(f"{valor}KB equivalen a {resultado:.2f}B")
  elif conversion == "Megabytes a Gigabytes":
    resultado = valor / 1024
    st.write(f"{valor}MB equivalen a {resultado:.2f}GB")
  elif conversion == "Gigabytes a Megabytes":
    resultado = valor * 1024
    st.write(f"{valor}GB equivalen a {resultado:.2f}MB")
  elif conversion == "Terabytes a Petabytes":
    resultado = valor / 1024
    st.write(f"{valor}TB equivalen a {resultado:.2f}PB")
  elif conversion == "Petabytes a Terabytes":
    resultado = valor * 1024
    st.write(f"{valor}PB equivalen a {resultado:.2f}TB")

# Página principal
def main():
  if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

  if not st.session_state.logged_in:
    login()
  else:
    menu()

if __name__ == "__main__":
  main()
