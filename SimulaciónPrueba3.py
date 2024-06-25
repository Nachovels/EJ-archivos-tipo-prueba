L1 = []
def RegistrarPedido():
    cliente = input("Nombre y apellido del cliente: ")
    L1.append(cliente)
    direccion = input("Ingrese dirección: ")
    L1.append(direccion)
    sector = input("Ingrese sector: ")
    L1.append(sector)
    kg_5 = 0
    kg_15 = 0
    kg_45 = 0
    while True: 
        
        print("1. Cilindro 5kg\n2. Cilindro 15kg\n3. Cilindro 45kg\n4.Terminar operación")
        cilindro = input("Ingrese opción: ")
        if cilindro == "1":
            kg_5 += 1
        elif cilindro == "2":
            kg_15+= 1
        elif cilindro == "3":
            kg_45+= 1
        elif cilindro == "4":
            print("Ingresando pedidos...")
            break
    L1.append(kg_5)
    L1.append(kg_15)
    L1.append(kg_45)
    
L = []
while True:
    print("***MENU***\n1. Registrar pedido\n2. Listar todos los pedidos\n3. Imprimir hoja de ruta\n4. Salir del programa")
    op = input("Seleccione opción: ")
    if op == "1": 
        RegistrarPedido()
        L.append(L1)
    elif op == "2": 
        print("Ingresando a opción 2...")
    elif op == "3": 
        print("Ingresando a opción 3...")
    elif op == "4": 
        print("Saliendo del programa...")
        break
    else:
        print("Ingrese una opción válida (1-4)")
print(L)