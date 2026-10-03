personas_dentro = 45
capacidad_maxima = 50

if personas_dentro < capacidad_maxima:
    print("Todavía pueden ingresar más personas.")
##########################
nivel_gasolina = 10  

if nivel_gasolina < 15:
    print("Alerta: Nivel de combustible bajo. Por favor, tanqueé pronto.")
############################
edad_cliente = 11

if edad_cliente < 12:
    print("El cliente aplica para la tarifa de 'Menú Infantil'.")

################################
temperatura_ambiente = -2

if temperatura_ambiente < 0:
    print("Cuidado: La temperatura está bajo el punto de congelación.")
###########################
intentos_fallidos = 2

if intentos_fallidos < 3:
    print("Puedes intentar ingresar tu clave nuevamente.")
else:
    print("Cuenta bloqueada por seguridad.")
    
    
################______>


edad = 21

if edad > 17:
    print("Acceso permitido: Eres mayor de edad.")
#######################
saldo = 500000
retiro = 200000

if saldo > retiro:
    print("Transacción aprobada. Procesando retiro...")
#####################################
velocidad_actual = 95
limite_maximo = 80

if velocidad_actual > limite_maximo:
    print("Alerta: Has superado el límite de velocidad permitido.")
########################################
ventas_mes = 120
meta_ventas = 100

if ventas_mes > meta_ventas:
    print("¡Felicidades! Has superado la meta y recibes una bonificación.")
###########################################
puntaje_actual = 2500
record_anterior = 2450

if puntaje_actual > record_anterior:
    print("¡Nuevo récord personal alcanzado!")
    
    
############_______<=


edad = 12
if edad <= 12:
    print("Aplica para la tarifa de niño.")
################
intentos = 3
limite_maximo = 3

if intentos <= limite_maximo:
    print("Aún puedes intentar ingresar.")
else:
    print("Cuenta bloqueada por seguridad.")
##################
costo_total = 50000
presupuesto = 50000
if costo_total <= presupuesto:
    print("Compra aprobada: El dinero es suficiente.")
###################
nota_final = 2.9

if nota_final <= 2.9:
    print("El estudiante debe presentar recuperación.")
#####################
peso_carga = 1000 # kg
limite_camion = 1000 # kg

if peso_carga <= limite_camion:
    print("El camión puede iniciar el viaje.")
else:
    print("Alerta: Exceso de peso.")
############# >=
edad = 18

if edad >= 18:
    print("Eres legalmente mayor de edad.")
############
nota = 3.0
minimo_aprobatorio = 3.0

if nota >= minimo_aprobatorio:
    print("Felicidades, has aprobado la materia.")
###############
ahorro_actual = 500000
meta_viaje = 500000

if ahorro_actual >= meta_viaje:
    print("¡Meta alcanzada! Ya tienes el dinero para tu viaje.")
########################
unidades_bodega = 25
pedido_cliente = 20

if unidades_bodega >= pedido_cliente:
    print("Pedido procesado: Tenemos existencias suficientes.")
#####################
temperatura_motor = 90

if temperatura_motor >= 90:
    print("Alerta: El sistema de enfriamiento debe activarse ahora.")
    
    
################# ==


password_guardada = "Admin123"
password_ingresada = "Admin123"

if password_ingresada == password_guardada:
    print("Acceso concedido.")
################
opcion = int(input("Seleccione (1: Iniciar, 2: Salir): "))

if opcion == 1:
    print("Iniciando el sistema...")
elif opcion == 2:
    print("Saliendo del programa.")
##################
tipo_usuario = "Premium"

if tipo_usuario == "Premium":
    print("Tienes acceso a contenido exclusivo sin anuncios.")
#################
respuesta_estudiante = 25
resultado_correcto = 5 * 5

if respuesta_estudiante == resultado_correcto:
    print("¡Respuesta correcta!")
######################
estado_servidor = "Activo"

if estado_servidor == "Activo":
    print("El servidor está respondiendo correctamente.")
######################  !=
usuario = ""

if usuario != "":
    print("Nombre de usuario registrado con éxito.")
else:
    print("Error: El campo de usuario no puede quedar vacío.")
############# 
pais_bloqueado = "Corea del Norte"
pais_usuario = "Colombia"

if pais_usuario != pais_bloqueado:
    print("Conexión permitida al servidor.")
#############
valor_anterior = 25
valor_actual = 28

if valor_actual != valor_anterior:
    print("Se detectó un cambio en la temperatura ambiente.")
###############
comando = "continuar"

if comando != "salir":
    print("El programa sigue en ejecución...")
###############
monto_enviado = 100.50
monto_recibido = 99.00

if monto_enviado != monto_recibido:
    print("Alerta: Hay una diferencia en los montos de la transacción.")

    
    