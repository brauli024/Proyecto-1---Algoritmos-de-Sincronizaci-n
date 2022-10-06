# SERVIDOR RELOJ
import socket
import datetime

print("************************* SERVIDOR RELOJ *************************")

s = socket.socket()  # creacion de scoket
print("Socket creado correctamente")

host = ''   # configuracion para todas las interfaces disponibles y con puerto 8000
port = 8000
s.bind((host, port))
s.listen(1)  # socket escuchando
print("Socket escuchando, listo para aceptar peticiones...")

while True:
    # creacion de nuevo objeto para acpetar y recibir peticiones
    connection, address = s.accept()
    data = connection.recv(1024)    # se recibe la solicitud del cliente
    if not data:
        break
    print("Conectado por: " + str(address) + "  -->  " + str(data))
    # se envia el tiempo que esta solicitando el cliente
    connection.send(str(datetime.datetime.now()).encode())
    connection.close()
