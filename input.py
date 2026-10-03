nombre = input("Por favor, ingresa tu nombre: ")
print(f"Bienvenido al sistema, {nombre}")
###########
edad_texto = input("¿Cuántos años tienes? ")
edad = int(edad_texto)
if edad >= 18:
    print("Puedes crear una cuenta.")
##############
password = input("Crea una contraseña: ")

if len(password) >= 8:
    print("Contraseña segura y guardada.")
else:
    print("Error: La contraseña debe tener al menos 8 caracteres.")
################
respuesta = input("¿Deseas guardar los cambios? (si/no): ").lower()

if respuesta == "si":
    print("Cambios guardados con éxito.")
elif respuesta == "no":
    print("Cambios descartados.")
else:
    print("Opción no reconocida.")
#################
puntos = input("Ingresa tu puntaje actual: ")

if puntos.isdigit():
    total = int(puntos) + 10
    print(f"Tu nuevo puntaje con bono es: {total}")
else:
    print("Error: Por favor ingresa solo números, no letras.")
    