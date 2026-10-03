nota = 4.5
if nota  >3.0:
    print("estudiante aprobo")

#################

clima=20
if clima >20:
    print("tempado")
    
##############

bodega = 30
if bodega >30:
    print("salida")

###################3

venta = 25
if venta >25:
    print("meta lograda")
else:
    print("toca vender")


#####################

aforo = 40
if aforo <40:
    print("Hay cupo")
else:

    print("aforo lleno")

# and 

temporatura= 24 
if temporatura >18 and temporatura <26:
    print("temperatura adecuada")
    
###############

nota = 3.2
if nota >0 and nota <3.2:
    print("no aprobo ")
########################
venta = 25
if venta >0 and venta < 25:
    print ("falta vender")
##########################

usuario = "usuario"
clave = "1456"
if usuario == "usuario" and clave == "1456":
    print("aprovado")
else:
    print("incorrecto")
############################

edad=20
tiene_licencia= True
if edad >=18 and tiene_licencia == True:
    print("Puede conducir")
else:
    print("no puede conducir")

#### OR ######
respuesta = input("¿Deseas salir? (si/s): ")

if respuesta == "si" or respuesta == "s":
    print("Cerrando el programa...")
    
##################
dia = "Sábado"

if dia == "Sábado" or dia == "Domingo":
    print("El horario de atención es de 10:00 AM a 2:00 PM.")
else:
    print("El horario de atención es de 8:00 AM a 6:00 PM.")
##################################
tiene_efectivo = False
tiene_tarjeta = True

if tiene_efectivo or tiene_tarjeta:
    print("Puedes realizar el pago.")
else:
    print("No tienes medios de pago disponibles.")
##################################
sensor_humo = False
sensor_calor = True
if sensor_humo == True or sensor_calor == True:
    print("ALERTA Se ha detectado una posible emergencia.")
###############################
edad = 65
es_estudiante = False
if edad >= 60 or es_estudiante == True:
    print("Tienes un 20% de descuento.")

###########____Not
nombre = ""
if not nombre:
    print("Error: El nombre no puede estar vacío.")
########################################################
tarea_completada = False

if not tarea_completada:
    print("Aún tienes tareas pendientes por realizar.")
#############################################
lista_negra = ["invitado123", "spam_user"]
usuario = "andres_dev"

if not usuario in lista_negra:
    print("Acceso permitido: El usuario es confiable.")

##########################################
luz_encendida = True

luz_encendida = not luz_encendida
print(f"¿La luz está encendida?: {luz_encendida}") 
##################################################
sistema_bloqueado = False

if not sistema_bloqueado:
    print("Iniciando transferencia de datos segura...")
else:
    print("Acción denegada: El sistema está bajo mantenimiento.")
    
############

    
    