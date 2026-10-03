edad_str = input("Ingresa tu edad: ")
edad = int(edad_str) 
if edad >= 18:
    print("Acceso permitido.")
    ######

precio_decimal = 199.99
precio_entero = int(precio_decimal)

print(precio_entero) 

##############
cantidad_texto = "50"
bono = 10

total = int(cantidad_texto) + bono
print(f"El total es: {total}") 

#############
es_valido = True
valor_numerico = int(es_valido)

print(valor_numerico) 
################

conteo_sensor = 10.7
personas_reales = int(conteo_sensor)

print(f"Hay {personas_reales} personas detectadas.") 

############# Float
precio_texto = input("¿Cuánto cuesta el aguacate? ")
precio = float(precio_texto) 
total = precio * 2
print(f"El total por dos unidades es: {total}")
###############
puntos = 10
puntos_decimal = float(puntos)

print(puntos_decimal) 
############
nota1 = 3.5
nota2 = 4.2
promedio = (nota1 + nota2) / 2

print(f"Tu promedio es: {float(promedio)}")
##########
valor_base = 100000
iva_texto = "0.19" 
iva_decimal = float(iva_texto)

impuesto = valor_base * iva_decimal
print(f"El valor del IVA es: {impuesto}")
#############
distancia_texto = "1.5e3" 
distancia = float(distancia_texto)

print(f"La distancia procesada es: {distancia} metros")
###################    str
edad = 20
mensaje = "Tu edad es: " + str(edad)
print(mensaje)
################
numero_cuenta = 10203040
digitos = len(str(numero_cuenta))
print(f"El número de cuenta tiene {digitos} dígitos.")
############
puntaje = 450
archivo_linea = "Puntaje final: " + str(puntaje)

################
esta_activo = True
estado_texto = str(esta_activo)

print("El estado del servidor es: " + estado_texto)
################
prefijo = "ID-"
consecutivo = 505
etiqueta_completa = prefijo + str(consecutivo)

print(f"La etiqueta del producto es: {etiqueta_completa}")
############# bool
nombre = "Wilson"
print(bool(nombre)) 

nombre_vacio = ""
print(bool(nombre_vacio))
################
saldo = 0
print(bool(saldo)) 

puntos = 150
print(bool(puntos)) 
################
sistema_encendido = True

if bool(sistema_encendido):
    print("El motor está funcionando.")
###############
comparacion = (10 > 5)
print(bool(comparacion))

############ print
precio_aguacate = 4500.50
print(f"El costo unitario es: ${precio_aguacate:,.2f}")
########
usuario = "Wilson"
print(f"Bienvenido al sistema, {usuario}. Hoy es lunes.")
#########
cantidad = 12
precio = 500
print(f"Total a pagar por {cantidad} unidades: ${cantidad * precio}")
###############
print("27", "04", "2026", sep="-") 
###########
nota = 4.0
print(f"Estado final: {'Aprobado' if nota >= 3.0 else 'Reprobado'}")

########## range

for i in range(5):
    print(f"Esta es la repetición número {i}")
    
###########

for anio in range(2020, 2025):
    print(f"Año: {anio}")
    
##########

for par in range(0, 11, 2):
    print(f"Número par: {par}")

############

for seg in range(10, 0, -1):
    print(f"Despegue en {seg}...")
print("¡Fuego!")
##########


