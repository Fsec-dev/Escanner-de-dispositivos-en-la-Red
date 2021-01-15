# Scanner-de-dispositivos-en-la-Red
Los siguientes Script nos muestran los dispositivos que se encuentran en nuestra Red y podremos ver que tipo de Hardware tienen.

En el repositorio tenemos 2 Script **scannerdevice_api.py** el cual usa una API para traducir la direccion MAC al nombre del dispositivo
Luego tenemos a **scannerRed.py** el cual usa un modulo para la operacion.

## Requerimientos para el uso de los Scripts
Los Scripts estan escritos en Python3 por lo tanto si tienes instalado Python3 en tu sistema no hay problema.

### Instalando modulos necesarios:
- ``python3 -m pip install requests``
- ``python3 -m pip install scapy``
- ``python3 -m pip install maclookup``

## Uso:
### Ejecutando Script scannerdevice_api.py
``sudo ./scannerdevice_api.py 192.168.0.0/24``
### Ejecutando Script scannerRed.py
``sudo ./scannerRed.py 192.168.0.0/24``

