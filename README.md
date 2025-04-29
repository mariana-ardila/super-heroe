#INICIO DEL JUEGO
print("----- Llamada de emergencia -----")
print("A las 7:30 se presentó un robo multimillonario en el banco central, el dinero robado estaba almacenado en el bloque TRP09.")
print("El gerente del banco decide contactar a Operación 73RT para resolver el caso.")

# LLAMADA DE EMERGENCIA 
print("\n--- Recepción de la llamada ---")
while True:
    try:
        respuesta = int(input("Gracias por contactar a Operación 73RT, ¿Cuál es tu emergencia? \n1) Robo \n2) Captura \n3) Asesinato \nElige (1, 2 o 3): "))
        if respuesta== 1 or 2 or 3:
            break
        else:
            print("Por favor elige una opción válida (1, 2 o 3).")
    except ValueError:
        print("Por favor ingresa un número.")

#SOLICITAR INFORMACIÓN
direccion = input("¿Dónde ocurre la emergencia? Escribe la dirección: ").upper()
print(f"\n-------- Ovnicoder va rumbo a {direccion} --------")
print(f"Ovnicoder ha llegado a {direccion}.")
print("Ovnicoder analiza la situación: La puerta está obstruida, el ladrón tiene rehenes y está armado.")


print("\n--- Situación de los rehenes ---")
while True:
    try:
        nrorehenes = int(input("¿Cuántos rehenes hay?, escribe el número: "))
        
        if nrorehenes <= 2:
            emergencia = input("¿Ovnicoder puede resolver la emergencia solo? (SI/NO): ").upper()
            if emergencia == "SI":
                print("\nOvnicoder se dirige a un pasillo con 3 oficinas cerradas. Solo puede entrar a una. Si ingresa a la que no es, todos pueden morir.")
                while True:
                    try:
                        oficina = int(input("¿A qué oficina entrarás? (1, 2 o 3): "))
                        if oficina == 1:
                            print("La oficina explota. ¡Todos mueren!")
                            resultado_final = "perdió"
                            break
                        elif oficina == 2:
                            print("¡Encontraste a los ladrones! ¡Ganaste!")
                            resultado_final = "gano"
                            break
                        elif oficina == 3:
                            print("La oficina está vacía. Los ladrones escaparon. ¡Perdiste!")
                            resultado_final = "vacio"
                            break
                        else:
                            print("Elige solo entre 1, 2 o 3.")
                    except ValueError:
                        print("Por favor ingresa un número.")
                break
            else:
                break

        elif nrorehenes >= 3:
            emergencia = input("¿Ovnicoder puede resolver la emergencia solo? (SI/NO): ").upper()
            if emergencia == "NO":
                print("Ovnicoder llama a operación 73RT y solicita 2 subonicoders de refuerzo.")
                print("En 10 segundos llegan los subonicoders de refuerzo.")
                print("\nOvnicoder y su equipo se dirigen a un pasillo con 3 oficinas cerradas. Solo pueden entrar a una.")
                while True:
                    try:
                        oficina = int(input("¿A qué oficina entrarán? (1, 2 o 3): "))
                        if oficina == 1:
                            print("La oficina explota. ¡Todos mueren!")
                            resultado_final = "perdió"
                            break
                        elif oficina == 2:
                            print("¡Encontraste a los ladrones! ¡Ganaste!")
                            resultado_final = "gano"
                            break
                        elif oficina == 3:
                            print("La oficina está vacía. Los ladrones escaparon. ¡Perdiste!")
                            resultado_final = "vacio"
                            break
                        else:
                            print("Elige solo entre 1, 2 o 3.")
                    except ValueError:
                        print("Por favor ingresa un número.")
                break
            else:
                break
        else:
            print("Número no válido, intenta de nuevo.")
    except ValueError:
        print("Por favor escribe un número.")
