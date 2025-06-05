from errores import FueraDeRango, NoExiste
from sistema import Sistema
sistema=Sistema()  

print("\n1. Registrar\n2. Listar\n3. Salir del sistema")
while True:
    try:
        menu=int(input("\nElija su accion a realizar: "))
        if menu<1 or menu>3:
            raise FueraDeRango
        break
    except ValueError:
        print("\nError!Elija un valor adecuado\n")
    except FueraDeRango:
        print("\nError!Elija un indice de los mostrados en pantalla\n")
while menu!=3:
    copia_piezas=sistema.lista_piezas

    while menu!=3:
        if menu==1:
            print("\nRegistrar:\n 1. Pieza\n 2. Maquina\n 3. Cliente\n 4. Pedido\n 5. Reposicion\n 6. Salir")
            while True:
                try:
                    registrar=int(input("\nIngrese indice de elemento a registrar: "))
                    if registrar<1 or registrar>6:
                        raise FueraDeRango
                    break
                except ValueError:
                    print("\nError! Ingrese un valor valido\n")
                except FueraDeRango:
                    print("\nError! Ingrese un indice dentro del rango\n")
            if registrar==1:
                abortar=False
                desc_pieza=input("Brinda una descripcion de la pieza: ")
                for i in sistema.lista_piezas:
                    if i.desc==desc_pieza:
                        nueva_desc=int(input("ERROR:La pieza ya existe.\n Si desea poner otra descripcion, ingrese 1\n Si desea abortar la operacion ingrese 2\n__:"))
                        if nueva_desc!=1 and nueva_desc!=2:
                            raise FueraDeRango

                        elif nueva_desc==1:
                            verificado=1
                            while verificado==1:
                                desc_pieza=input("Ingrese una descripcion valida: ")
                                for j in sistema.lista_piezas:
                                    if desc_pieza==j.desc:
                                        print("\nERROR!La descripcion de la pieza sigue siendo igual\n")
                                    else:
                                        verificado=2

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
                        
                while True:
                    try:
                        lote_pieza=int(input("Brinda el tamaño del lote de reposicion: "))
                        break
                    except ValueError:
                        print("\nError!Elija un valor adecuado\n")
                        
                while True:
                    try:
                        cantidad_pieza=int(input("Brinda una nueva cantidad inicial de piezas: "))
                        break
                    except ValueError:
                        print("\nError!Elija un valor adecuado\n")
                        

                sistema.registrar_pieza(desc_pieza,costo_pieza,cantidad_pieza,lote_pieza)
            elif registrar==2:
                while True:
                    try:
                        descripcion_maquina=input("Ingrese la descripcion de la nueva maquina: ")
                        abortar=False
                        for i in sistema.lista_maquinas:
                            if i.desc==descripcion_maquina:
                                while True:
                                    try:
                                        nueva_desc=int(input("ERROR:La maquina ya existe.\n Si desea poner otra descripcion, ingrese 1\n Si desea abortar la operacion ingrese 2\n__:"))
                                        if nueva_desc!=1 and nueva_desc!=2:
                                            raise FueraDeRango
                                        elif nueva_desc==1:
                                            verificado=1
                                            descripcion_maquina=input("Ingrese una nueva descripcion valida para la maquina: ")
                                            while verificado==1:
                                                for j in sistema.lista_maquinas:
                                                    if j.desc == descripcion_maquina:
                                                        print("ERROR! La descripcion sigue siendo igual")
                                                        break
                                                    else:
                                                        verificado=2
                                        elif nueva_desc==2:
                                            abortar=True
                                        break
                                    except ValueError:
                                        print("\nError!Elija un valor adecuado\n")
                                    except FueraDeRango:
                                        print("\nError!Valor de indice fuera de rango\n")
                            if abortar:
                                break
                        break
                    except ValueError:
                        print("\nError!Elija un valor adecuado\n")

                maquina0=sistema.registrar_maquina(descripcion_maquina)

                print("Comenzemos con sus requerimientos...\n")
                
                
                                  
                nuevo_requerimiento=1
                while nuevo_requerimiento==1:
                    if copia_piezas==[]:
                            print("\nError! No existen piezas registradas, no se puede registrar maquinas\n")
                            break
                    for i in copia_piezas:
                        print(f"\n Codigo: {i.codigo}\n Descripcion: {i.desc}\n Costo: {i.costo}\n Cantidad: {i.cantidad}\n Lote: {i.lote}\n")  
                    while True:
                        try:
                            code=int(input("ingrese el codigo de la pieza requerida: "))
                            break
                        except ValueError:
                            print("\nError!Elija un valor adecuado\n")
                    nueva_pieza=None
                    for i in copia_piezas:
                        if i.codigo==code:
                            nueva_pieza=i
                            copia_piezas.remove(i)
                    while nueva_pieza is None:
                        print("El codigo no pertenece a ninguna pieza")
                        while True:
                            try:
                                code=int(input("ingrese el codigo de la pieza requerida: "))
                                break
                            except ValueError:
                                print("\nError!Elija un valor adecuado\n")
                                
                        for i in sistema.lista_piezas:
                            if i.codigo==code:
                                nueva_pieza=i
                                copia_piezas.remove(i)
                    while True:
                        try:
                            cantidad_piezas=int(input("Ingrese la cantidad de piezas necesarias: "))
                            break
                        except ValueError:
                            print("\nError!Elija un valor adecuado\n")
                    nuevo_req=sistema.registrar_requerimiento(maquina0,nueva_pieza,cantidad_piezas)
                    maquina0.agregar_requerimiento(nuevo_req)
                    
                    while True:
                        try:
                            nuevo_requerimiento=int(input("Desea agregar un nuevo requerimiento?\n 1.SI\n 2.NO\n___:"))
                            if nuevo_requerimiento!=1 and nuevo_requerimiento!=2:
                                raise FueraDeRango
                            break
                        except ValueError:
                            print("\nError!Elija un valor adecuado\n")
                      
                        except FueraDeRango:
                            print("\nError! Indice fuera de rango")
        
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
                sistema.listar_piezas()
                while True:
                    try:
                        code=int(input("Ingrese el codigo de la Pieza que desea reponer: "))
                        noexiste=True
                        for i in sistema.lista_piezas:
                            if code==i.codigo:
                                pieza_repuesta=i
                                noexiste=False
                        if noexiste:
                            raise NoExiste
                        
                        break
                    except ValueError:
                        print("\nError! Elija un valor adecuado\n")
                    except NoExiste:
                        print("\nError! Ese codigo de pieza no existe\n")
                        

                while True:
                    try:
                        cantidad_lotes=int(input("Ingrese la cantidad de lotes a reabastecer: "))
                        break
                    except ValueError:
                        print("\nError! Elija un valor adecuado\n")
                        pass
                sistema.registrar_reposicion(pieza_repuesta,cantidad_lotes)
            elif registrar==6:
                        pass
        elif menu==2:
            print("\nListar: \n 1. Clientes\n 2. Pedidos\n 3. Maquinas\n 4. Piezas\n 5. Contabilidad\n 6. Salir")
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
                    sistema.listar_maquinas()
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
        print("\n1. Registrar\n2. Listar\n3. Salir del sistema")
        while True:
            try:
                menu=int(input("\nElija su accion a realizar: "))
                if menu<1 or menu>3:
                    raise FueraDeRango
                break
            except ValueError:
                print("\nError!Elija un valor adecuado\n")
            except FueraDeRango:
                print("\nError!Elija un indice de los mostrados en pantalla\n")