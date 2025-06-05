from entities.errores import FueraDeRango, NoExiste, YaExiste
from entities.Sistema import Sistema
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
                while True:
                    try:
                        desc_pieza=input("Brinda una descripcion de la pieza: ")
                        for i in sistema.lista_piezas:
                            if i.desc==desc_pieza:
                                raise YaExiste
                        nueva_desc=1
                        break
                    except YaExiste:
                        print("\nError! Esa pieza ya existe. Elija una nueva descripcion\n")
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
                print("\nPieza registrada con exito!\n")
            elif registrar==2:
                copia_piezas=sistema.lista_piezas.copy()
                if copia_piezas==[]:
                            print("\nError! No existen piezas registradas, no se puede registrar maquinas\n")
                            break
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
                            if copia_piezas==[]:
                                break
                            nuevo_requerimiento=int(input("Desea agregar un nuevo requerimiento?\n 1.SI\n 2.NO\n___:"))
                            if nuevo_requerimiento!=1 and nuevo_requerimiento!=2:
                                raise FueraDeRango
                            break
                        except ValueError:
                            print("\nError!Elija un valor adecuado\n")
                      
                        except FueraDeRango:
                            print("\nError! Indice fuera de rango")
                print("\nMaquina registrada con exito!\n")
        
            elif registrar==3:
                print("\nRegistrar cliente: ")
                print("Tipo cliente: \n 1. Cliente Particular \n 2. Empresea")
                while True:
                    try:
                        tipo=int(input("Seleccione tipo de cliente: "))
                        if tipo!=1 and tipo!=2:
                            raise FueraDeRango
                        break
                    except ValueError:
                        print("\nError! Ingrese un valor valido\n")
                    except FueraDeRango:
                        print("\nError! Indice fuera de rango\n")
                if tipo==1:
                    while True:
                        try:
                            cédula= int(input("ingrese la cédula del cliente: "))
                            for particular in sistema.lista_particulares:
                                if particular.cédula==cédula:
                                    raise YaExiste
                            break
                        except YaExiste:
                            print("ERROR: la cédula ya está regitrada. Ingrese una nueva")
                        except ValueError:
                             print("\nError! Ingrese un valor valido\n")
                    nombre=input("ingrese nombre completo del cliente: ")
                    while True:
                        try:
                            teléfono=int(input("ingrese el teléfono del cliente: "))
                            break
                        except ValueError:
                             print("\nError! Ingrese un valor valido\n")
                    correo_electrónico= input("ingrese el correo electrónico del cliente: ")
                    sistema.registrar_cliente_Particular(cédula, nombre, teléfono, correo_electrónico)
                    print("\nCliente Particular registrado con exito!\n")
    
                elif tipo==2:
                    while True:
                        try:
                            rut=int(input("Ingrese número de RUT: "))
                            for empresa in sistema.lista_empresas:
                                if empresa.rut==rut:
                                    raise YaExiste
                            break
                        except ValueError:
                            print("\nError! Elija un valor adecuado\n")
                        except YaExiste:
                            print("ERROR: el RUT ya está regitrado, ingrese uno nuevo")                  
                    nombre=input("Ingrese nombre: ")
                    página_web=input("Ingrese página web: ")
                    while True:
                        try:
                            teléfono=int(input("Ingrese teléfono de contacto: "))
                            break
                        except ValueError:
                            print("\nError! Ingrese un valor valido\n")
                    correo_electrónico= input("ingrese el correo electrónico del cliente: ")
                    sistema.registrar_cliente_Empresa(rut, nombre, teléfono, correo_electrónico, página_web)
                    print("\nCliente Empresa registrado con exito!\n")
                    
            elif registrar==4:
                if sistema.lista_clientes==[]:
                    print("\nError! No existen clientes para poder registrar pedidos\n")
                    break
                elif sistema.lista_maquinas==[]:
                    print("\nError! No existen maquinas para poder registrar pedidos\n")
                    break
                cliente_pedido=None
                maquina_pedido=None
                print("seleccione el cliente que desea registrar un pedido: ")
                for cliente in sistema.lista_clientes:
                    print(f"ID: {cliente.id} Nombre: {cliente.nombre}, ")
                while True:
                    try:
                        seleccion_cliente = int(input("Ingrese el ID del cliente: "))
                        break
                    except ValueError:
                        print("\nError! Elija un valor adecuado\n")
                for cliente in sistema.lista_clientes:
                    if cliente.id == seleccion_cliente:
                        cliente_pedido = cliente
                
                print("seleccione la máquina que desea registrar un pedido: ")
                for maquina in sistema.lista_maquinas:
                    print(f"Código: {maquina.codigo}, descripción: {maquina.descripcion}")
                while True:
                    try:
                        seleccion_maquina = int(input("Ingrese el código de la maquina a registrar: "))
                        break
                    except ValueError:
                        print("\nError! Elija un valor adecuado\n")
                for maquina in sistema.lista_maquinas:
                    if maquina.codigo == seleccion_maquina:
                        maquina_pedido = maquina
                sistema.registrar_pedido(cliente_pedido,maquina_pedido)
                print("\nPedido registrado con exito!\n")
                
            elif registrar==5:
                if sistema.lista_piezas==[]:
                    print("\nError! No existen piezas para reabastecer\n")
                    break
                for i in sistema.lista_piezas:
                    print(f"\n Codigo: {i.codigo}\n Descripcion: {i.desc}\n Costo: {i.costo}\n Cantidad: {i.cantidad}\n Lote: {i.lote}\n")  
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
                sistema.registrar_reposicion(pieza_repuesta,cantidad_lotes)
                print("\nReposicion realizada con exito!\n")
            elif registrar==6:
                        pass
        elif menu==2:
            print("\nListar: \n 1. Clientes\n 2. Pedidos\n 3. Maquinas\n 4. Piezas\n 5. Contabilidad\n 6. Salir")
            while True:
                try:
                    listar=int(input("\nIngrese indice de elemento a listar: "))
                    if listar<1 or listar>6:
                        raise FueraDeRango
                    break
                except FueraDeRango:
                    print("\nError! Elija un indice dentro del rango\n")
                except ValueError:
                    print("\nError! Elija un valor adecuado\n")
            
            if listar==1:
                if sistema.lista_clientes==[]:
                    print("\nError! No existen clientes para listar\n")
                    break
                sistema.listar_clientes()

            elif listar==2:
                    if sistema.lista_pedidos==[]:
                        print("\nError! No existen pedidos para listar\n")
                        break
                    print("Desea filtrar los pedidos segun su estado de entrega?\n\n1.SI\n2.NO")

                    while True:
                        try:
                            filtrado=int(input("Ingrese su eleccion: "))
                            if filtrado!=1 and filtrado!=2:
                                raise FueraDeRango
                            break       
                        except FueraDeRango:
                            print("\nError! Elija un indice dentro del rango\n")
                        except ValueError: 
                            print("\nError! Elija un valor valido\n")
                    if filtrado==1:
                        print("Elija que Pedidos desea ver:\n\n 1.Pendientes\n 2.Entregados\n")
                        while True:
                            try:
                                tipo_pedido=int(input("Ingrese su eleccion: "))
                                if tipo_pedido!=1 and tipo_pedido!=2:
                                    raise FueraDeRango
                                break
                            except FueraDeRango:
                                print("\nError! Elija un indice dentro del rango\n")
                            except ValueError:
                                print("\nError! Elija un valor valido\n")
                        sistema.listar_pedidos_filtrados(tipo_pedido)
                    elif filtrado==2:
                        sistema.listar_pedidos()
                    
            elif listar==3:
                    sistema.listar_maquinas()
            elif listar==4:
                    sistema.listar_piezas()
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
