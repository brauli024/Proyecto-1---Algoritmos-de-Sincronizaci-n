# SERVIDOR RELOJ
import socket
import datetime

print("****************************** NODO MAESTRO ******************************")

s = socket.socket()  # creacion de scoket
print("Socket creado correctamente")

host = ''   # configuracion para todas las interfaces disponibles y con puerto 8000
port = 8000
s.bind((host, port))
s.listen(5)  # socket escuchando
print("Iniciando proceso de sincronizacion...")

lista = []  # contiene el mensaje que se recibe de los esclavos separado por  palabras
dict = {}   # Diccionario que contiene los esclavos existentes con su respectiva hora
numSinc = []    # Lista con los esclavos existentes


while True:
    # creacion de nuevo objeto para acpetar y recibir peticiones
    connection, address = s.accept()
    data = connection.recv(1024).decode()   # se recibe el mensaje del cliente
    if not data:
        break
    lista = data.split()    # mensaje separado por pakabras
    dict[lista[0]] = lista[1] + " " + lista[2]  # se guarda el tiempo recibido
    # tserver: tiempo del nodo maestro
    tserver = datetime.datetime.now() - \
        datetime.datetime.strptime(
            str(lista[1]+" 00:00:00.000000"), '%Y-%m-%d %H:%M:%S.%f')

    # si todos los esclavos ya fueron sincronizados con el ultimo tiempo
    # calculado, se inicia un nuevo proceso de sincronizacion
    if len(numSinc) == 0:
        print("\nINICIANDO SINCRONIZACION...")
        print("Tmaster:  " + str(tserver))
        print("Tslaves:  " + str(dict))
        numSinc = list(dict)    # se actualiza numSinc

    print("\nConectado por: " + str(address) +
          "  -->  " + "Proceso: " + lista[0])

    # si todos los esclavos ya fueron sincronizados con el ultimo tiempo
    # calculado, se procede a hacer un nueva estimacion de tprom
    if len(numSinc) == len(dict.keys()):
        print("Estimando tiempo de sincronizacion...")
        tprom = tserver
        for key in dict.keys():
            tclient = datetime.datetime.strptime(dict[key], '%Y-%m-%d %H:%M:%S.%f') - \
                datetime.datetime.strptime(
                    str(lista[1]+" 00:00:00.000000"), '%Y-%m-%d %H:%M:%S.%f')
            tprom = tprom + tclient
        tprom = tprom/(len(dict.keys())+1)
        tprom = datetime.datetime.strptime(
            lista[1]+" "+str(tprom), '%Y-%m-%d %H:%M:%S.%f')

    # se envia el tiempo calculado a los esclavos
    connection.send(str(tprom).encode())
    print("Tiempo que sera transmitido:  " + str(tprom))
    connection.close()

    # seccion encargada de eliminar de numSinc los esclavos que van
    # siendo sincronizados
    for num in numSinc:
        if num == lista[0]:
            numSinc.pop(numSinc.index(num))
            print("Proceso " + lista[0] + " sincronizado correctamente")
