  # Tarea 02 - OUILookup

## Descripción

Introducción
El programa OUILookup.py es una herramienta desarrollada para consultar información sobre los fabricantes de dispositivos mediante la dirección MAC (Media Access Control) proporcionada. Utiliza la API OUI (Organizationally Unique Identifier) para obtener el fabricante correspondiente a la dirección MAC ingresada por el usuario, y presenta el resultado junto con el tiempo de respuesta. Además, se implementan opciones de línea de comandos que permiten buscar direcciones MAC específicas o consultar fabricantes de la tabla ARP de la red local.

Este programa se ha implementado utilizando el lenguaje de programación Python, y hace uso de la biblioteca requests para interactuar con la API externa.

Requerimientos
Python 3: El código está diseñado para funcionar en Python 3, y se recomienda tener la versión 3.6 o superior.
Bibliotecas: Se utiliza la biblioteca requests para hacer peticiones HTTP a la API OUI.
Sistema Operativo: El programa puede ejecutarse tanto en sistemas operativos Windows como Linux.
Descripción del Programa
El programa OUILookup.py funciona de la siguiente manera:

Entrada de Parámetros:

El programa acepta parámetros de la línea de comandos mediante el uso de getopt.
Los parámetros disponibles son:
--mac <mac_address>: Para ingresar una dirección MAC y consultar el fabricante correspondiente.
--arp: Para mostrar la lista de fabricantes que están presentes en la tabla ARP de la red local.
Consulta a la API OUI:

Cuando se ingresa una dirección MAC válida a través del parámetro --mac, el programa realiza una consulta a la API pública OUI, que devuelve información sobre el fabricante asociado a esa dirección MAC.
Si la consulta es exitosa, el programa muestra la dirección MAC, el nombre del fabricante y el tiempo de respuesta de la consulta.
Si la dirección MAC proporcionada tiene un formato incorrecto, el programa genera un mensaje de error.
Opción --arp:

Esta opción (si está implementada) permite consultar la tabla ARP de la red local y obtener información sobre los fabricantes asociados a las direcciones MAC presentes en esa tabla.
Diagrama de Flujo
El diagrama de flujo para la implementación del programa sigue la estructura lógica del código, mostrando cómo el flujo de trabajo depende de las entradas del usuario y de la consulta a la API OUI. El diagrama es útil para comprender cómo las diferentes partes del programa se interrelacionan y cómo se manejan las decisiones, como la validación de la MAC y la consulta a la API.

import requests
import getopt
import sys
import time

def consultar_oui(mac):
    # URL de la API OUI
    url = f"https://api.macvendors.com/{mac}"
    
    try:
        # Realiza la consulta
        inicio = time.time()
        respuesta = requests.get(url)
        tiempo_respuesta = (time.time() - inicio) * 1000  # tiempo en milisegundos

        if respuesta.status_code == 200:
            # Si la consulta fue exitosa, muestra el fabricante y el tiempo de respuesta
            fabricante = respuesta.text
            print(f"MAC address : {mac}")
            print(f"Fabricante : {fabricante}")
            print(f"Tiempo de respuesta: {round(tiempo_respuesta, 2)}ms")
        else:
            print("Error: No se encontró información para esta MAC.")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["mac=", "arp"])
    except getopt.GetoptError:
        print("Error: Parámetro no válido.")
        sys.exit(1)
    
    # Procesar opciones
    for opt, arg in opts:
        if opt == "--mac":
            # Si el parámetro es --mac, llamamos a la función para consultar la MAC
            mac = arg.strip().lower()
            consultar_oui(mac)
        elif opt == "--arp":
            # Si el parámetro es --arp, puede implementarse para mostrar la tabla ARP
            print("Mostrar la tabla ARP aquí (funcionalidad no implementada).")
        else:
            print("Error: Parámetro no reconocido.")
            sys.exit(1)

if __name__ == "__main__":
    main()

Explicación del Código
Función consultar_oui(mac):

Esta función toma como entrada una dirección MAC, realiza una consulta HTTP a la API OUI, y muestra el fabricante asociado a la dirección MAC.
La API OUI devuelve el nombre del fabricante en formato de texto plano. Si la consulta es exitosa, el programa muestra la dirección MAC, el nombre del fabricante y el tiempo de respuesta de la consulta.
Función main():

Esta función gestiona los parámetros de la línea de comandos utilizando getopt. Dependiendo del parámetro ingresado (--mac o --arp), el programa realizará diferentes acciones.
Si el parámetro es --mac, el programa llama a la función consultar_oui(mac) con la dirección MAC proporcionada.
Si el parámetro es --arp, se muestra un mensaje indicando que esta funcionalidad no está implementada (aunque se podría extender en el futuro para mostrar la tabla ARP local).
Manejo de Errores:

El código maneja errores como un formato incorrecto de la dirección MAC o problemas con la conexión a la API OUI. Si la API no devuelve un código de estado 200, se muestra un mensaje de error.
Recomendaciones y Mejoras Futuras
Implementación de la opción --arp:

Actualmente, la funcionalidad --arp no está implementada. Se podría agregar la capacidad de leer la tabla ARP local y obtener información sobre las direcciones MAC de los dispositivos conectados en la red.
Manejo de formatos más flexibles:

El programa podría ser más flexible al aceptar diferentes formatos de entrada para las direcciones MAC (por ejemplo, con guiones, sin guiones, en mayúsculas, etc.).
Optimización de la conexión a la API:

Actualmente, se utiliza un único hilo para realizar la consulta. Se podría mejorar el rendimiento utilizando conexiones asíncronas para realizar múltiples consultas simultáneamente si fuera necesario.
Conclusión
El programa OUILookup.py es una herramienta sencilla pero útil para consultar información sobre los fabricantes de dispositivos mediante su dirección MAC. La implementación es flexible y permite fácilmente futuras mejoras, como la integración de la funcionalidad --arp o la optimización de la interacción con la API externa.
