# PROCESO EN LA MAQUINA CLIENTE
import socket
import datetime
import time
import sys
print("************************* PROCESO EN LA MAQUINA CLIENTE - ESCLAVOS *************************")

term = ""  # mensaje que sera enviado al nodo maestro
while True:
    s = socket.socket()  # creacion de scoket

    host = 'localhost'  # configuracion para localhost y puerto 8000
    port = 8000
    s.connect((host, port))  # creando conexion

    # se crea term = id_esclavo fecha_esclavo hora_esclavo
    # sys.argv[1] es el parametro que se pasa al ejecutar el programa
    term = str(sys.argv[1]) + " " + str(datetime.datetime.now())
    s.sendall(str(term).encode())   # se manda el mensaje al nodo maestro
    tserver = s.recv(1024)  # se recibe el tiempo calculado por el nodo maestro
    tserver = datetime.datetime.strptime(
        tserver.decode(), '%Y-%m-%d %H:%M:%S.%f')
    # strptime -> tserver se pasa a un formato datetime.datetime
    print('Tiempo recibido  ' + str(tserver))

    time.sleep(5)
    print('\n')
