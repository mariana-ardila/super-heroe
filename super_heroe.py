"""
A las 7:30 se presentó un robo multimillonario en el banco central, el dinero robado estaba almacenado en el bloque TRP09
El gerente del banco decide contactar Operación 73RT para que resolviera el caso
"""
print ("-----Llamada de emergencia-----") 
respuesta = int(input("Gracias por ponerte en contacto con Operación 73RT, ¿Cual es tu emergencia? \n1) robo \n2) captura \n3) asesinato \n"))
if respuesta == 1 or respuesta == 2 or respuesta == 3:
    print("¿Donde es la emergencia?")
    direccion = input ("Dirección: ").upper()
    print("¿Necesitas refuerzos?")
    refuerzo = input ("Refuerzos: ")


print (f"--------OVNICODER VA RUMBO A {direccion}--------")
print(f"Ovnicoder llegó a {direccion} ")
print("Al llegar Ovnicoder analiza la situación\nOvnicoder se da de cuenta que la puerta está obstruida, el ladrón tiene rehenes y esta armado")
rehenes=0
while True:
     try:
         
        nrorehenes = int (input("escribe nro rehenes: "))
        if rehenes <=2 :
            print("Ovnicoder resuelve la emergencia solo")
        
        elif rehenes >= 3: 
            print ("Ovnicoder solicita refuerzos a Operación y empieza a actuar")
            continue
        break

     except ValueError:
            print("No actua y espera refuerzos")
    
disponible =input("¿necesitas que lleve refuerzos? ")    


if disponible == "si":
    print ("ya voy para alla, ¿necesitas que lleve apoyo?") 
    
else:
    print("estoy llegando") 
    

vuelo = input("¿podre volar tan rapido? ")
    
if vuelo == "si":
    print ("necesito volar como nunca lo he hecho")
    
else:
    print ("Volare hasta un punto cercano y luego camino para no alertar mi llegada")    


print("Ovnicoder llega al sitio, analizando, mirando la situacion para ver como actua")


       