import requests
import ezodf
import os

nombre_archivo = 'BD.ods'
log_file = 'log.txt'

def descargar_archivo(url, nombre_archivo):
    response = requests.get(url)
    if response.status_code == 200:
        with open(nombre_archivo, 'wb') as file:
            file.write(response.content)
        with open(log_file, 'a') as log:
            log.write(f"El archivo {nombre_archivo} se ha descargado correctamente.\n")
    else:
        with open(log_file, 'a') as log:
            log.write(f"Error al descargar el archivo {nombre_archivo}. Código de respuesta: {response.status_code}\n")
        
# Descargar el archivo ODS desde la URL
descargar_archivo('https://raw.githubusercontent.com/Netzahualcoyotl/webejemplo/main/BD.ods', nombre_archivo)

if os.path.exists(nombre_archivo):
    print("El archivo se ha descargado correctamente.")
else:
    print("Hubo un error al descargar el archivo.")

def abrir_archivo(nombre_archivo):
    try:
        doc = ezodf.opendoc(nombre_archivo)
        hoja = doc.sheets['Hoja1']
        filas = []
        for row in hoja.rows():
            fila = []
            for cell in row:
                if cell.value is None:
                    fila.append("")
                else:
                    fila.append(cell.value)
            filas.append(fila)
        columnas = filas.pop(0)
        return columnas, filas
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")
        
# Llamar a la función abrir_archivo para verificar si el archivo puede ser abierto correctamente
columnas, filas = abrir_archivo(nombre_archivo)
if columnas is not None and filas is not None:
    print("El archivo se abrió correctamente.")
else:
    print("Error al abrir el archivo.")

def buscar_valores(nombre, numero):
    columnas, filas = abrir_archivo(nombre_archivo)
    resultados = []
    resultados.append(columnas)    
    for fila in filas[1:]: # saltar la fila de encabezado
        if fila[18] == nombre:
            try:
                if int(fila[19]) == int(numero):
                    resultados.append(fila)
            except ValueError:
                 if fila[21] == numero:
                    resultados.append(fila)
    
    if not resultados:
        return {'mensaje': 'No se encontraron resultados para la búsqueda.'}
    #return {'resultados': resultados}
    return {'nombres_columnas': columnas, 'valores': resultados}

