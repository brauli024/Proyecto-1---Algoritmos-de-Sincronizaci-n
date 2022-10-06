# PROCESO EN LA MAQUINA CLIENTE
import socket
import datetime

codificacion = 'utf-8'
print("************************* PROCESO EN LA MAQUINA CLIENTE *************************")

s = socket.socket()  # creacion de scoket
print("Socket creado correctamente")

host = 'localhost'  # configuracion para localhost y puerto 8000
port = 8000
s.connect((host, port))  # creando conexion
print("Conectando...")

t0 = datetime.datetime.now()  # t0: hora en la que el cliente envio la peticion
print("Envio de solicitud en el tiempo t0:  " + str(t0))

s.sendall(b'Solicitud para obtener la hora')    # se manda la solicitud
tserver = s.recv(1024)  # tserver:  tiempo que regresa el servidor de tiempo
print(str(tserver))
tserver = datetime.datetime.strptime(tserver.decode(), '%Y-%m-%d %H:%M:%S.%f')

t1 = datetime.datetime.now()  # t1: hora en la que el cliente recibio la respuesta
print("Respuesta de solicitud en el tiempo t1:  " + str(t1))

print('Hora de reloj devuelta por el servidor:  ' + str(tserver))

tclient = tserver + (t1-t0)/2   # calculo - nuevo tiempo para ser sincronizado
print('AJUSTE - hora del reloj sincronizado:  ' + str(tclient))
