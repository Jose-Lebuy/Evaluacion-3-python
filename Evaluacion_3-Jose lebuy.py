
precios_asientos=(60000,80000,50000)

pasajes_comprados_comun=[]
pasajes_comprados_con_espacio=[]
pasajes_comprados_sin_reclinar=[]
total=[]

disponibles_comun=["A6","A7","A8","A9","A19","A20","A21","A22","A23","A24","A25","A26","A27","A28","A29","A30","A31","A32","A33",
                   "B6","B7","B8","B9","B19","B20","B21","B22","B23","B24","B25","B26","B27","B28","B29","B30","B31","B32","B33",
                   "C6","C7","C8","C9","C19","C20","C21","C22","C23","C24","C25","C26","C27","C28","C29","C30","C31","BC2","C33",
                   "D6","D7","D8","D9","D19","D20","D21","D22","D23","D24","D25","D26","D27","D28","D29","D30","D31","D32","D33",
                   "E6","E7","E8","E9","E19","E20","E21","E22","E23","E24","E25","E26","E27","E28","E29","E30","E31","E32","E33",
                   "F6","F7","F8","F9","F19","F20","BF1","F22","F23","F24","F25","F26","F27","F28","F29","F30","F31","F32","F33"
                   ]
disponibles_espacio_pies=[
                            "A1","A2","A3","A4","A5","A18",
                            "B1","B2","B3","B4","B5","B18",
                            "C1","C2","C3","C4","C5","C18",
                            "D1","D2","D3","D4","D5","D18",
                            "E1","E2","E3","E4","E5","E18",
                            "F1","F2","F3","F4","F5","F18"

                          ]

disponibles_sin_reclinar=[  "A10","A17",
                            "B10","B17",
                            "C10","C17",
                            "D10","D17",
                            "E10","E17",
                            "F10","F17"                  
                        ]

def registrar_usuarios():
    while True:
        
        try:
            rut=int(input("Ingrese rut"))
            if rut >9999999 and rut < 99999999:
                print("Operacion realizada exitosamente")
                break
            else:
                print("Rut no valido, Vuelve a intentar")
        except:
            print("Ingrese solo numeros")
        
    while True:

        print("Seleccione tipo de asiento, Tipo de asiento disponibles:\n")
        print("A) Asiento común ----> $60.000 pesos")
        print("B) Espacio adicional para piernas ----> $80.000 pesos")
        print("C) Asiento sin reclinar ----> $50.000 pesos")
        tipo_aiento=input("Seleccione opcion").upper()
        if tipo_aiento==("A"):
        
            print(disponibles_comun[0:114])
            asiento=input("Seleccione asiento disponible:").upper()
            if asiento in disponibles_comun:
                print("Compra realizada")
                disponibles_comun.remove(asiento)
                pasajes_comprados_comun.append(asiento)
                ganancias=+50000
                total.append(ganancias)
            else:
                print("Asiento no existe, ingrese denuevo")

        elif tipo_aiento==("B"):
            print(disponibles_espacio_pies[0:36])
            asiento_con=input("Seleccione asiento disponible:").upper()
            if asiento_con in disponibles_espacio_pies:
                print("Compra realizada")
                ganancias=+80000
                total.append(ganancias)
                disponibles_espacio_pies.remove(asiento_con)
                pasajes_comprados_con_espacio.append(asiento_con)
            else:
                print("Asiento no existe, ingrese denuevo")
        
        elif tipo_aiento==("C"):
            print(disponibles_sin_reclinar[0:12])
            asiento_sin=input("Seleccione asiento disponible:").upper()
            if asiento_sin in disponibles_sin_reclinar:
                print("Compra realizada")
                ganancias=+40000
                total.append(ganancias)
                disponibles_sin_reclinar.remove(asiento_sin)
                pasajes_comprados_sin_reclinar.append(asiento_sin)
            else:
                print("Asiento no existe, ingrese denuevo")
        else:
            print("Seleccione una opcion disponible")
        mas_asientos=input("Deseas comprar mas? SI/NO:\n").upper()
        if mas_asientos == "SI":
            print("Volviendo a menu de seleccion")
        elif mas_asientos == "NO":
            break


def mostrar_ubicacion_disponibles():
    while True:    
        print("Espacios disponibles")
        print("A) Comun")
        print("B) Con espacio para pies")
        print("C) Sin reclinar")
        print("D) Volver atras")
        opcion_ver=input("Ingrese opcion").upper()
        if opcion_ver=="A":
            print(disponibles_comun[0:114])
        elif opcion_ver=="B":
            print(disponibles_espacio_pies[0:36])
        elif opcion_ver=="C":
            print(disponibles_sin_reclinar[0:12])
        elif opcion_ver=="D":
            break
            
def lista_pasajeros():
    print("Lista de pasajeros")
    print(pasajes_comprados_comun)
    print(pasajes_comprados_con_espacio)
    print(pasajes_comprados_sin_reclinar)

    




# menu principal
while True:
    print("A) Comprar pasajes")
    print("B) Mostrar ubicaciones disponibles")
    print("C) Ver listado de pasajeros")
    print("D) Buscar pasajero")
    print("E) Mostrar ganancias totales")
    print("F) Salir")
    opcion=input("Seleccione opcion:").upper()
    if opcion == "A":
        registrar_usuarios()
    elif opcion == "B":
        mostrar_ubicacion_disponibles()
    elif opcion == "C":
        lista_pasajeros()
    elif opcion == "E":
        print(total)
    elif opcion == "F":
        break