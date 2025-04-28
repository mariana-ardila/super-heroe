"""
A las 7:30 se presentó un robo multimillonario en el banco central, el dinero robado estaba almacenado en el bloque TRP09
Un sospechoso está implicado en el robo
El gerente del banco decide contactar Operación 73RT para que resolviera el caso

************* Bienvenido a la operación 73RT **************
"""
print ("Espera a que uno de nuestros Ovnicoders te conteste: ")      

vuelo = ""
disponible = ""
contesta = input("¿El superheroe contesta?")


while True:
     try:    
        if contesta == "si":
            opcion=int(input("Gracias por ponerte en contacto, tenemos muchos poderes para resolver tu caso con uno de nuestros Ovnicoders, selecciona una opción dependiendo del súper poder que necesites: \n1.Volar\n2.fuerza\n3.super velocidad")).Isdigit ()
            if opcion == 1:
                print("volaré al lugar de los hechos y empezaré a buscar por todos los bloques")
                
            elif opcion == 2:
                print("")
            
            elif opcion == 3:
            
            else:
                print("opcion no valida")
                
            break
     
        else: 
            print ("El súper heroe está ocupado. ")
        break

     except ValueError:
            print("el telefono suena, nadie contesta")
    
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
