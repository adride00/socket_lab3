import socket

TCP_IP = '172.20.3.232'
TCP_PORT = 8080
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print '*****LISTA DE COMANDOS****'
print '1) arquitectura: muestra la arquitectura del sistema'
print '2) version: muestra la version de debian'
print '3) memoria: muestra el uso de memoria'
print '4) cpu: muestra la informacion del cpu'
print '5) permisos: mustra permisos de direcctorios y ficheros'
print '6) particiones: muestra las particiones del disco duro'
print '7) usuario: muestra el nombre de usuario del sistema'
print '8) directorio: muestra el directorio actual de trabajo'
print '9) fecha: muestra la fecha actual'
print '10) apagar: apaga el sistema'

while True:
    data = s.recv(20000)
    print 'Server' , str(data)
    
    msg = raw_input('>>>>')
    
    if msg != 0:
        s.send(msg)
        print "sent "
        
    else:
        break
        print 'bye '
        s.close()
