# -*- coding: utf-8 -*-

# Formateador de scripts .sql para mejorar la legibilidad de los mismos
# Añade saltos de línea después de cada coma y de cada punto y coma
# Autor: Angel Padilla
# Fecha: 02/13/2024
# version: 0.1.0

# Importación de módulos necesarios
import re
import sys

def formatear_sql(archivo_entrada, archivo_salida):
    # Abro archivo y lo copio a otro
    with open(archivo_entrada, 'r') as entrada:
        datosEntrada = entrada.read()

    comaNoSeguidaDeSalto = r',(?!\n)'
    patronSustitucionComas= ',\n'
    contenido_formateado = re.sub(comaNoSeguidaDeSalto, patronSustitucionComas , datosEntrada)

    puntoYcomaNoSeguidaDeSalto =r';(?!\n)'
    patronSustitucionPuntoYComa=r';\n'
    contenido_formateado = re.sub(puntoYcomaNoSeguidaDeSalto, patronSustitucionPuntoYComa , contenido_formateado)

    with open(archivo_salida, 'w') as salida:
        salida.write(contenido_formateado)

# Parámetros de entrada
archivo_entrada = sys.argv[1]
archivo_salida = sys.argv[2]

formatear_sql(archivo_entrada, archivo_salida)
print("Copia formateada creada con éxito.")