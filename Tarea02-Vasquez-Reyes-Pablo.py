import urllib.request
import json
import time
import getopt
import sys


# Función para obtener el fabricante a partir de la dirección MAC
def obtener_fabricante_por_mac(mac):
    url = f"https://api.maclookup.app/v2/macs/{mac}"  # URL de la API
    try:
        # Realizamos la consulta a la API
        with urllib.request.urlopen(url) as response:
            data = json.load(response)  # Convertimos la respuesta en JSON
            # Extraemos el fabricante, o un mensaje de error si no se encuentra
            fabricante = data.get("vendor", "Not found")
            return fabricante
    except Exception as e:
        return f"Error: {e}"


# Función para procesar y completar direcciones MAC
def normalizar_mac(mac):
    # Remover espacios y convertir a minúsculas
    mac = mac.replace(" ", "").lower()
    # Asegurarse de que la dirección MAC tenga 12 caracteres (sin los dos puntos o guiones)
    if len(mac) < 12:
        # Si la MAC tiene menos de 12 caracteres, completamos con ceros al final
        mac = mac.ljust(12, "0")
    # Formato con guiones
    return ':'.join([mac[i:i+2] for i in range(0, 12, 2)])


# Función para procesar los argumentos de la línea de comandos
def procesar_argumentos():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "m:a:", ["mac=", "arp="])
        return opts
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)


# Función para manejar el flujo principal
def main():
    opts = procesar_argumentos()

    # Comprobamos si el argumento --mac está presente
    for opt, arg in opts:
        if opt in ("-m", "--mac"):
            mac_normalizada = normalizar_mac(arg)
            start_time = time.time()  # Marca el tiempo de inicio
            fabricante = obtener_fabricante_por_mac(mac_normalizada)
            end_time = time.time()  # Marca el tiempo de fin
            tiempo_respuesta = round((end_time - start_time) * 1000)  # Calcula el tiempo en ms

            # Mostramos el resultado
            print(f"MAC address : {mac_normalizada}")
            print(f"Fabricante : {fabricante}")
            print(f"Tiempo de respuesta: {tiempo_respuesta}ms")


if __name__ == "__main__":
    main()
