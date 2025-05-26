print("\n1. Registrar\n2. Listar\n3. Salir del sistema")
menu=int(input("\nElija su accion a realizar: "))
if menu<1 or menu>3:
    raise ValueError
while menu!=3:
    if menu==1:
        print("\nRegistrar:\n 1. Pieza\n 2. Maquina\n 3. Cliente\n 4. Pedido\n 5. Reposicion\n 6. Salir")
        registrar=int(input("\nIngrese indice de elemento a registrar: "))
        if registrar<1 or registrar>6:
            raise ValueError
    elif menu==2:
        print("\nListar: \n 1. Clientes\n 2. Pedidos\n 3. Cliente\n 4. Pedido\n 5. Reposicion\n 6. Salir")
        listar=int(input("\nIngrese indice de elemento a listar: "))
        if listar<1 or listar>6:
            raise ValueError
    print("\n1. Registrar\n2. Listar\n3. Salir del sistema")
    menu=int(input("\nElija nuevamente su accion a realizar: "))

print('prueba')
