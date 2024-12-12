# Tarea 02 - OUILookup

## Descripción

El programa **OUILookup** permite consultar información sobre direcciones MAC. Usando el estándar **OUI (Organizationally Unique Identifier)**, el programa identifica el fabricante de una dirección MAC proporcionada por el usuario. Este software está implementado para ser ejecutado en sistemas operativos **Linux** y **Windows** y sigue el paradigma de programación funcional. Utiliza la librería **requests** para interactuar con una API que devuelve información sobre el fabricante de la dirección MAC.

## Instrucciones

### Requisitos

- **Python 3.x** o superior
- **requests** (módulo de Python)

Para instalar las dependencias necesarias, puedes ejecutar:

```bash
pip install requests
python3 OUILookup.py --mac <direccion_mac>
python3 OUILookup.py --mac 98:06:3c:92:ff:c5
MAC address : 98:06:3c:92:ff:c5
Fabricante : Samsung Electronics Co.,Ltd
Tiempo de respuesta: 17ms
python3 OUILookup.py --arp

