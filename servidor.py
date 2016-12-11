# -*- coding: utf-8 -*-
import socket
import sys
import os
import subprocess
from subprocess import *
from thread import * #agregmos los paquetesde la programacion por hilos

funciones={
        'arquitectura':'arch',
        'version':     ['uname', '-r'],
        'memoria': ['cat', '/proc/meminfo'],
        'cpu': ['cat', '/proc/cpuinfo'],
        'permisos': ['ls', '-lh'],
        'particiones': ['df', '-h'],
        'usuario': ['hostname'],
        'directorio': ['pwd'],
        'fecha': ['date'],
        'apagar': ['shutdown', '-h', 'now']
}

palabras={
       'pupusas': 'Comida tipica salvadoreña, hecha con masa de arroz o maiz rellenas de diferentes ingredientes',
       'socket': 'concepto abstracto por lo cual dos programas puedan intercambiar cualquier flujo de datos',
       'algoritmo': 'Conjunto de operaciones sistematicas que permite hacer un calculo y hallar la solucion a un tipo de problemas',
       'sql': 'Es un lenguaje especifico del dominio que da acceso a un sistema de gestion de bases de datos relacionales',
       'mysql': 'Es un sistema de gestion de bases de datos relacionales, considerada la base de datos open source mas popular del mundo.',
       'mongodb': 'Es un sistema de bases de datos NoSQL o no relacionales orientado a documentos, desarrollado bajo el concepto de codigo abierto.',
       'servidor': 'Es un ordenador o maquina informatica que esta al servicio de otras maquinas, ordenadores o personas llamadas clientes.',
       'python': 'Lenguaje de programacion interpretado cuya filosofia hace incapie en una sintaxis que favorezca un codigo legible.',
       'botnet': 'Termino que hace referencia a un conjunto de red de robots informaticos o bots, que se ejecutan de manera autonomo o automatica.',
       'nube': 'Modelo de almacenamiento de datos basado en redes de computadoras, donde los datos estan alojados en espacios de almacenamiento virtualizados.'  
                  
           

}
HOST = '' #Escuchar por todas las interfaces
PORT = 8080 #Usamos un puerto de numeracion alta para no interferir

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket Creado'

try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print 'Error al crear Socket. Error code: ' + str(msg[0]) + ' , Mensaje de error: ' + msg[1]
    sys.exit()
print ' Enlace via socket activo'

s.listen(10) #Encolar un maximo de 10 conexiones
print 'Socket escuchando en puerto ' + str(PORT)

def enviar_funcion(data):
    comando=funciones[data]
    print comando
    res=subprocess.check_output(comando)
    conn.send(str(res))

def enviar_palabra(data):
    palabra=palabras[data]
    conn.send(palabra)    
def hilo_cliente(conn):
    #Enviar un mensaje al clientecuando se conecte
    conn.send('Bienvenido al server, Escriba algo y precione intro')
    
    #Ciclo

    
    while True:
        
        data = conn.recv(20000)
        
        print data
        if palabras.has_key(data):
            enviar_palabra(data)
            continue
        if funciones.has_key(data):
            enviar_funcion(data)
            continue
        newdata = raw_input('>>>')
        conn.send(newdata)    
    conn.close()

while 1:
    #Espere para aceptar la conexion
    conn, addr = s.accept()
    print 'Conectado con ' + addr[0] + ':' +str(addr[1])

    # Inicia un nuevo hilo el cual recibe dos parametros y la conexion
    start_new_thread(hilo_cliente, (conn,))
        
s.close()
