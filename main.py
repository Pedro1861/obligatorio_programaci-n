from exceptions.Errores import FueraDeRango
from entities.Sistema import Sistema

print("\n1. Registrar\n2. Listar\n3. Salir del sistema")
menu=int(input("\nElija su accion a realizar: "))
while menu!=3:
    if menu<1 or menu>3:
        raise ValueError
    while menu!=3:
        if menu==1:
            print("\nRegistrar:\n 1. Pieza\n 2. Maquina\n 3. Cliente\n 4. Pedido\n 5. Reposicion\n 6. Salir")
            registrar=int(input("\nIngrese indice de elemento a registrar: "))
            if registrar<1 or registrar>6:
                raise ValueError
            if registrar==1:
                desc_pieza=input("Brinda una descripcion de la pieza: ")
                for i in Sistema.lista_piezas:
                    if i.desc==desc_pieza:
                        nueva_desc=int(input("ERROR:La pieza ya existe.\n Si desea poner otra descripcion, ingrese 1\n Si desea abortar la operacion ingrese 2"))
                        if nueva_desc!=1 and nueva_desc!=2:
                            raise FueraDeRango

                        if nueva_desc==1:
                            desc_pieza=input("Ingrese una descripcion valida: ")
                            while  desc_pieza==i.desc:
                                print("ERROR: La descripcion sigue siendo igual")
                                desc_pieza=input("Ingrese una descripcion valida: ")

                        elif nueva_desc==2:
                            break
                            

                costo_pieza=int(input("Brinda costo por unidad de la pieza: "))
                lote_pieza=int(input("Brinda el tamanio del lote de reposicion: "))
                cantidad_pieza=int(input("Brinda un cantidad inicial de piezas: "))
                Sistema.registrar_pieza()
            elif registrar==2:
                pass
            elif registrar==3:
                pass
            elif registrar==4:
                pass
            elif registrar==5:
                pass
            elif registrar==6:
                pass
        elif menu==2:
            print("\nListar: \n 1. Clientes\n 2. Pedidos\n 3. Cliente\n 4. Pedido\n 5. Reposicion\n 6. Salir")
            listar=int(input("\nIngrese indice de elemento a listar: "))
            if listar<1 or listar>6:
                raise ValueError
        print("\n1. Registrar\n2. Listar\n3. Salir del sistema")
        menu=int(input("\nElija nuevamente su accion a realizar: "))