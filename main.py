from exceptions.Errores import FueraDeRango
from entities.Sistema import Sistema
sistema=Sistema()  

print("\n1. Registrar\n2. Listar\n3. Salir del sistema")
menu=int(input("\nElija su accion a realizar: "))
while menu!=3:
    if menu<1 or menu>3:
        raise FueraDeRango
    while menu!=3:
        if menu==1:
            print("\nRegistrar:\n 1. Pieza\n 2. Maquina\n 3. Cliente\n 4. Pedido\n 5. Reposicion\n 6. Salir")
            registrar=int(input("\nIngrese indice de elemento a registrar: "))
            if registrar<1 or registrar>6:
                raise FueraDeRango
            if registrar==1:
                abortar=False
                desc_pieza=input("Brinda una descripcion de la pieza: ")
                for i in sistema.lista_piezas:
                    if i.desc==desc_pieza:
                        nueva_desc=int(input("ERROR:La pieza ya existe.\n Si desea poner otra descripcion, ingrese 1\n Si desea abortar la operacion ingrese 2\n__:"))
                        if nueva_desc!=1 and nueva_desc!=2:
                            raise FueraDeRango

                        if nueva_desc==1:
                            desc_pieza=input("Ingrese una descripcion valida: ")
                            while  desc_pieza==i.desc:
                                print("ERROR: La descripcion sigue siendo igual")
                                desc_pieza=input("Ingrese una descripcion valida: ")

                        elif nueva_desc==2:
                            abortar=True
                            break
                if abortar: 
                    continue
                while True:
                    try:
                        costo_pieza=int(input("Brinda costo por unidad de la pieza: "))
                        break
                    except ValueError:
                        print("\nError!Elija un valor adecuado\n")
                        costo_pieza=int(input("Brinda un nuevo costo por unidad de la pieza: "))
                while True:
                    try:
                        lote_pieza=int(input("Brinda el tamanio del lote de reposicion: "))
                        break
                    except ValueError:
                        print("\nError!Elija un valor adecuado\n")
                        lote_pieza=int(input("Brinda el tamanio del lote de reposicion: "))
                while True:
                    try:
                        cantidad_pieza=int(input("Brinda una nueva cantidad inicial de piezas: "))
                        break
                    except ValueError:
                        print("\nError!Elija un valor adecuado\n")
                        cantidad_pieza=int(input("Brinda una nueva cantidad inicial de piezas: "))

                sistema.registrar_pieza(desc_pieza,costo_pieza,cantidad_pieza,lote_pieza)
            elif registrar==2:
                print("Comenzemos con sus requerimientos...\n")
                print(Sistema.lista_piezas)
                code=int(input("ingrese el codigo de la pieza requerida: "))
                nuevo_requerimiento=1
                while nuevo_requerimiento==1:
                    nueva_pieza=0
                    for i in Sistema.lista_piezas:
                        if i.codigo==code:
                            nueva_pieza=i
                    while nueva_pieza==0:
                        print("El codigo no pertenece a ninguna pieza")
                        while True:
                            try:
                                code=int(input("ingrese el codigo de la pieza requerida: "))
                                break
                            except ValueError:
                                print("\nError!Elija un valor adecuado\n")
                                code=int(input("ingrese el codigo de la pieza requerida: "))
                        for i in Sistema.lista_piezas:
                            if i.codigo==code:
                                nueva_pieza=i
                    while True:
                        try:
                            cantidad_piezas=int(input("Ingrese la cantidad de piezas necesarias: "))
                            break
                        except ValueError:
                            print("\nError!Elija un valor adecuado\n")
                            cantidad_piezas=int(input("Ingrese la cantidad de piezas necesarias: "))  
                    while True:
                        try:
                            nuevo_requerimiento=int(input("Desea agregar un nuevo requerimiento?\n 1.SI\n 2.NO\n___:"))
                            if nuevo_requerimiento!=1 and nuevo_requerimiento!=2:
                                raise FueraDeRango
                            break
                        except ValueError:
                            print("\nError!Elija un valor adecuado\n")
                            nuevo_requerimiento=int(input("Desea agregar un nuevo requerimiento?\n 1.SI\n 2.NO\n___:"))
                        except FueraDeRango:
                            print("\nError! Indice fuera de rango")
                            nuevo_requerimiento=int(input("Desea agregar un nuevo requerimiento?\n 1.SI\n 2.NO\n___:"))
                            
                    
                    
                pass
            elif registrar==3:
                while True:
                    try:
                        pass
                    except:
                        pass
            elif registrar==4:
                while True:
                    try:
                        pass
                    except:
                        pass
            elif registrar==5:
                while True:
                    try:
                        pass
                    except:
                        pass
            elif registrar==6:
                while True:
                    try:
                        pass
                    except:
                        pass
        elif menu==2:
            print("\nListar: \n 1. Clientes\n 2. Pedidos\n 3. Cliente\n 4. Pedido\n 5. Reposicion\n 6. Salir")
            listar=int(input("\nIngrese indice de elemento a listar: "))
            if listar<1 or listar>6:
                raise ValueError
            elif listar==1:
                    while True:
                        try:
                            pass
                        except:
                            pass
            elif listar==2:
                    while True:
                        try:
                            pass
                        except:
                            pass
            elif listar==3:
                    while True:
                        try:
                            pass
                        except:
                            pass
            elif listar==4:
                    while True:
                        try:
                            pass
                        except:
                            pass
            elif listar==5:
                    while True:
                        try:
                            pass
                        except:
                         pass
            elif listar==6:
                pass
        elif menu==3:
            break
        print("\n1. Registrar\n2. Listar\n3. Salir del sistema")
        menu = int(input("\nElija su accion a realizar: "))