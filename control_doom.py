import serial
import pyautogui
import time

# !!! CONFIGURACIÓN PRINCIPAL !!!
# Cambia 'COM3' por el puerto real donde se conecta tu ESP32 (lo ves en el IDE de Arduino)
PUERTO_SERIAL = 'COM3' 
BAUD_RATE = 115200

try:
    esp32 = serial.Serial(PUERTO_SERIAL, BAUD_RATE, timeout=0.1)
    print(f" Conectado exitosamente al ESP32 en el puerto {PUERTO_SERIAL}")
    print("Esperando la palabra mágica 'DOOM' en el circuito...")
except Exception as e:
    print(f"❌ Error al conectar: {e}. Revisa el puerto COM en el administrador de dispositivos.")
    exit()

modo_juego_activo = False
ultimo_pot = 2048

while True:
    try:
        if esp32.in_waiting > 0:
            # Leer línea enviada por el ESP32
            linea = esp32.readline().decode('utf-8', errors='ignore').strip()
            
            if not modo_juego_activo:
                if "START_DOOM" in linea:
                    print("¡PALABRA DOOM DETECTADA! Iniciando simulación de controles...")
                    modo_juego_activo = True
                    # Aquí podrías automatizar la apertura del juego si quisieras
            else:
                # Procesar controles si ya estamos dentro del juego
                if linea.startswith("POT:"):
                    try:
                        valor_pot = int(linea.split(":")[1])
                        
                        # Lógica de Giro: Si mueves la perilla a la izquierda o derecha
                        # Simulamos presionar las flechas del teclado o las teclas A / D
                        if valor_pot < 1500:
                            pyautogui.keyDown('left')   # Gira a la izquierda
                            pyautogui.keyUp('right')
                        elif valor_pot > 2600:
                            pyautogui.keyDown('right')  # Gira a la derecha
                            pyautogui.keyUp('left')
                        else:
                            pyautogui.keyUp('left')     # Zona muerta central (Quieto)
                            pyautogui.keyUp('right')
                    except:
                        pass
                        
                elif "DISPARO" in linea:
                    print("🎤 ¡Grito detectado! ¡FUEGO!")
                    pyautogui.press('ctrl') # En el Doom clásico se dispara con la tecla Ctrl izquierdo
                    # O si juegas una versión moderna, puedes cambiarlo por: pyautogui.click()
                    
    except KeyboardInterrupt:
        print("\nPrograma finalizado por el usuario.")
        break

esp32.close()