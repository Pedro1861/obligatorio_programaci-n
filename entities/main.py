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
                                        print("\nEEROR!La descripcion de la pieza sigue siendo igual\n")
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
                        lote_pieza=int(input("Brinda el tamanio del lote de reposicion: "))
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
                print("\nRegistrar cliente: ")
                print("Tipo cliente: \n 1. Cliente Particular \n 2. Empresea")
                try:
                    tipo=int(input("Seleccione tipo de cliente: "))
                except ValueError:
                    print("ERROR: Ingrese un número válido (1 o 2).")
                if tipo==1:
                    try:
                        cédula= int(input("ingrese la cédula del cliente: "))
                    except ValueError:
                        print("ERROR: Ingrese un número válido para la cédula.")
                    for particular in sistema.lista_particulares:
                        while particular.cédula == cédula:
                            cédula=int(input("ERROR: la cédula ya está regitrada. \n Ingrese una nueva cédula: "))
                    nombre=input("ingrese nombre completo del cliente: ")
                    try:
                        teléfono=int(input("ingrese el teléfono del cliente: "))
                    except ValueError:
                        print("ERROR: Ingrese un número válido para el teléfono.")
                    correo_electrónico= input("ingrese el correo electrónico del cliente: ")
                    sistema.registrar_cliente_Particular(cédula, nombre, teléfono, correo_electrónico)
    
                elif tipo==2:
                    try:
                        rut=int(input("Ingrese número de RUT: "))
                    except ValueError:
                        print("ERROR: Ingrese un número válido para el RUT.")
                    for empresa in sistema.lista_empresas:
                        while empresa.rut == rut:
                            rut=int(input("ERROR: el RUT ya está regitrado. \n Ingrese un nuevo número de RUT: "))                    
                    nombre=input("Ingrese nombre: ")
                    página_web=input("Ingrese página web: ")
                    try: 
                        teléfono=input("Ingrese teléfono de contacto: ")
                    except ValueError:
                        print("ERROR: Ingrese un número válido para el teléfono.")
                    correo_electrónico= input("ingrese el correo electrónico del cliente: ")
                    sistema.registrar_cliente_Empresa(rut, nombre, página_web, teléfono, correo_electrónico)

            elif registrar==4:
                cliente_pedido=None
                maquina_pedido=None
                print("sleccione el cliente que desea registrar un pedido: ")
                for cliente in sistema.lista_clientes:
                    print(f"ID: {cliente.ID_cliente} Nombre: {cliente.nombre}, ")
                try:
                    seleccion_cliente = int(input("Ingrese el ID del cliente: "))
                except ValueError:
                    print("ERROR: Ingrese un número válido para el ID del cliente.")
                for cliente in sistema.lista_clientes:
                    if cliente.ID_cliente == seleccion_cliente:
                        cliente_pedido = cliente
                
                print("sleccione la máquina que desea registrar un pedido: ")
                for maquina in sistema.lista_maquinas:
                    print(f"Código: {maquina.codigo}, descripción: {maquina.descripcion}")
                try:
                    seleccion_maquina = int(input("Ingrese el código de la maquina a registrar: "))
                except ValueError:
                    print("ERROR: Ingrese un número válido para el código de la máquina.")
                for maquina in sistema.lista_maquinas:
                    if maquina.codigo == seleccion_maquina:
                        maquina_pedido = maquina
                sistema.registrar_pedido(cliente_pedido,maquina_pedido)
                
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
