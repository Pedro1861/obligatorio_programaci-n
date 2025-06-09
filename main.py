from entities.fueraderango import FueraDeRango
from entities.noexiste import NoExiste
from entities.yaexiste import YaExiste
from entities.sistema import Sistema

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
    except :
        print("\nERROR INESPERADO: ingrese un nuevo valor\n")
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
                except :
                    print("\nERROR INESPERADO: ingrese un nuevo valor\n")
            if registrar==1:
                abortar=False
                while True:
                    try:
                        desc_pieza=input("Brinda una descripcion de la pieza: ")
                        for i in sistema.lista_piezas:
                            if i.desc==desc_pieza:
                                raise YaExiste
                        if desc_pieza=="":
                            raise ValueError
                        break
                    except ValueError:
                        print("\nError! La descripcion no puede estar vacia. Elija una nueva descripcion\n")
                    except YaExiste:
                        print("\nError! Esa pieza ya existe. Elija una nueva descripcion\n")
                        print("Desea ingresar una nueva descripcion? \n 1.SI \n 2.NO")
                        while True:
                            try:
                                opcion=int(input("Seleccione una opcion: "))
                                if opcion!=1 and opcion!=2:
                                    raise FueraDeRango
                                elif opcion==1:
                                    break
                                elif opcion==2:
                                    abortar=True
                                    print("\nOperación cancelada.\n")
                                    break
                                break
                            except ValueError:
                                print("\nError!Elija un valor adecuado\n")
                            except FueraDeRango:
                                print("\nError!Elija un indice de los mostrados en pantalla\n")
                            except :
                                print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                        if abortar:
                            break
                    except :
                        print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                if abortar:
                    continue
                while True:
                    try:
                        costo_pieza=int(input("Brinda costo por unidad de la pieza en USD: "))
                        if costo_pieza<0:
                            raise FueraDeRango
                        break
                    except ValueError:
                        print("\nError!Elija un valor adecuado\n")
                    except FueraDeRango:
                        print("\nError! El costo no puede ser negativo\n")
                    except :
                        print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                        
                while True:
                    try:
                        lote_pieza=int(input("Brinda el tamaño del lote de reposición: "))
                        if lote_pieza<0:
                            raise FueraDeRango
                        break
                    except ValueError:
                        print("\nError!Elija un valor adecuado\n")
                    except FueraDeRango:
                        print("\nError! El lote no puede ser negativo\n")
                    except :
                        print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                        
                while True:
                    try:
                        cantidad_pieza=int(input("Brinda una nueva cantidad inicial de piezas: "))
                        if cantidad_pieza<0:
                            raise FueraDeRango
                        break
                    except ValueError:
                        print("\nError!Elija un valor adecuado\n")
                    except FueraDeRango:
                        print("\nError! La cantidad no puede ser negativa\n")
                    except :
                        print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                
                        

                sistema.registrar_pieza(desc_pieza,costo_pieza,cantidad_pieza,lote_pieza)
                print("\nPieza registrada con exito!\n")
            elif registrar==2:
                copia_piezas=sistema.lista_piezas.copy()
                if copia_piezas==[]:
                    print("\nError! No existen piezas registradas, no se puede registrar maquinas\n")
                    break
                abortar=False
                while True:
                    try:
                        descripcion_maquina=input("Ingrese la descripcion de la nueva maquina: ")
                        if descripcion_maquina=="":
                            raise ValueError
                        for i in sistema.lista_maquinas:
                            if i.desc==descripcion_maquina:
                                raise YaExiste
                        break
                    
                    except ValueError:
                        print("\nError! La descripcion no puede estar vacia. Elija una nueva descripcion\n")
                    
                    except YaExiste:
                        print("\nError! Esa maquina ya existe. Elija una nueva descripcion\n")
                        print("Desea ingresar una nueva descripcion? \n 1.SI \n 2.NO")
                        while True:
                            try:
                                opcion=int(input("Seleccione una opcion: "))
                                if opcion!=1 and opcion!=2:
                                    raise FueraDeRango
                                elif opcion==1:
                                    continue
                                elif opcion==2:
                                    abortar=True
                                    print("Operación cancelada.")
                                    break
                        
                            
                            except ValueError:
                                print("\nError!Elija un valor adecuado\n")
                            except FueraDeRango:
                                print("\nError!Elija un indice de los mostrados en pantalla\n")
                            except :
                                print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                        if abortar:
                            break
                    except :
                        print("\nERROR INESPERADO: ingrese un nuevo valor\n")   
                if abortar:
                    continue

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
                            nueva_pieza=None
                            code=int(input("ingrese el codigo de la pieza requerida: "))
                            for i in copia_piezas:
                                if i.codigo==code:
                                    nueva_pieza=i
                                    copia_piezas.remove(i)
                            if nueva_pieza is None:
                                raise NoExiste
                            break
                        except ValueError:
                            print("\nError!Elija un valor adecuado\n")
                        except NoExiste:
                            print("\nERROR: El codigo no pertenece a ninguna pieza\n")
                        except :
                            print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                    
                
                    while True:
                        try:
                            cantidad_piezas=int(input("Ingrese la cantidad de piezas necesarias: "))
                            if cantidad_piezas<0:
                                raise FueraDeRango
                            break
                        except ValueError:
                            print("\nError!Elija un valor adecuado\n")
                        except FueraDeRango:
                            print("\nError! La cantidad no puede ser negativa\n")
                        except :
                            print("\nERROR INESPERADO: ingrese un nuevo valor\n")
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
                        except :
                            print("\nERROR INESPERADO: ingrese un nuevo valor\n")

                print("\nMaquina registrada con exito!\n")
        
            elif registrar==3:
                print("\nRegistrar cliente: ")
                print("Tipo cliente: \n 1. Cliente Particular \n 2. Empresa")
                while True: 
                    try:
                        tipo=int(input("Seleccione tipo de cliente: "))
                        if tipo!=1 and tipo !=2:
                            raise FueraDeRango
                        break
                    except ValueError:
                        print("\nERROR: Ingrese un número válido (1 o 2).\n")
                    except FueraDeRango:
                        print("\nERROR: Ingrese un número válido (1 o 2).\n")
                    except :
                        print("\nERROR INESPERADO: ingrese un nuevo valor\n")
            
                if tipo==1:
                    abortar=False
                    while True:
                        try:
                            cédula= int(input("ingrese la cédula del cliente: "))
                            if cédula<0:
                                raise ValueError
                            for i in sistema.lista_particulares:
                                if i.cedula==cédula:
                                    raise YaExiste
                            if len(str(cédula)) != 8:
                                raise FueraDeRango
                            break
                        except ValueError:
                            print("\nERROR: Ingrese un número válido para la cédula.\n")
                        except FueraDeRango:
                            print("\nERROR: La cédula debe tener 8 dígitos.\n")
                        except YaExiste:
                            print("\nERROR: La cédula ya está registrada.\n")
                            print("Desea ingresar una nueva cédula? \n 1.SI \n 2.NO")
                            while True:
                                try:
                                    opcion=int(input("Seleccione una opción: "))
                                    if opcion!=1 and opcion!=2:
                                        raise FueraDeRango
                                    elif opcion==1:
                                        break
                                    elif opcion==2:
                                        abortar=True
                                        print("Operación cancelada.")
                                        break
                                except ValueError:
                                    print("\nERROR: Ingrese un número válido (1 o 2).\n")
                                except FueraDeRango:
                                    print("\nERROR: Ingrese un número válido (1 o 2).\n")
                                except :
                                    print("\nERROR INESPERADO: ingrese un nuevo valor\n")

                            if abortar:
                                break
                        except :
                            print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                    if abortar:
                        continue
                       
                    while True:
                        try:
                            teléfono = input("Ingrese el teléfono celular del cliente (asegurese que comience con 09): ")

                            if not teléfono.isdigit():
                                raise ValueError
                            if not teléfono.startswith("09"):
                                raise NoExiste
                            if len(teléfono) != 9:
                                raise FueraDeRango
                            break

                        except ValueError:
                            print(f"\nERROR: Ingrese un número válido para el teléfono(>0).\n")
                        except NoExiste:
                            print("\nERROR: El teléfono debe comenzar con 09.\n")
                        except FueraDeRango:
                            print("\nERROR: El teléfono debe tener 9 dígitos.\n")
                        except :
                            print(f"\nERROR INESPERADO: ingrese un nuevo valor\n")
                        
                    while True:
                        try:
                            nombre=input("ingrese nombre completo del cliente: ")
                            if nombre=="":
                                raise ValueError
                            break
                        except ValueError:
                            print("\nError! El nombre no puede estar vacio. Elija un nuevo nombre\n")
                        except :
                            print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                    
                        
                    while True:
                        try:
                            correo_electrónico= input("ingrese el correo electrónico del cliente: ")
                            if correo_electrónico=="":
                                raise ValueError
                            if "@" not in correo_electrónico:
                                raise ValueError
                            break
                        except ValueError:
                            print("\nERROR: Ingrese un correo electrónico válido.\n")
                        except :
                            print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                    print("Cliente registrado con éxito!")

                    sistema.registrar_cliente_Particular(cédula, nombre, teléfono, correo_electrónico)
                    

                elif tipo==2:
                    abortar=False
                    while True:
                        try:
                            rut=int(input("Ingrese un número de RUT de 11 digitos: "))
                            if rut<0:
                                raise ValueError
                            for i in sistema.lista_empresas:
                                if i.RUT==rut:
                                    raise YaExiste
                            if len(str(rut)) !=11:
                                raise FueraDeRango
                            break
                        except FueraDeRango:
                            print("\nERROR: El RUT debe tener 11 dígitos.\n")
                        except ValueError:
                            print("\nERROR: Ingrese un número válido para el RUT.\n")
                        except YaExiste:
                            print("\nERROR: El RUT ya está registrado.\n")
                            print("Desea ingresar un nuevo RUT? \n 1.SI \n 2.NO")
                            while True:
                                try:
                                    opcion=int(input("Seleccione una opción: "))
                                    if opcion!=1 and opcion!=2:
                                        raise FueraDeRango
                                    elif opcion==1:
                                        break
                                    elif opcion==2:
                                        abortar=True
                                        print("Operación cancelada.")
                                        break
                                except ValueError:
                                    print("\nERROR: Ingrese un número válido (1 o 2).\n")
                                except FueraDeRango:
                                    print("\nERROR: Ingrese un número válido (1 o 2).\n")
                                except :
                                    print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                            if abortar:
                                break
                        except :
                            print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                    if abortar:
                        continue
                    while True:
                        try:
                            nombre=input("Ingrese nombre: ")
                            if nombre=="":
                                raise ValueError
                            break
                        except ValueError:
                            print("\nERROR: Ingrese un nombre válido.\n")
                        except :
                            print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                    while True:
                        try:
                            página_web=input("Ingrese página web: ")
                            if página_web=="":
                                raise ValueError
                            break
                        except ValueError:
                            print("\nERROR: Ingrese una página web válida.\n")
                        except :
                            print("\nERROR INESPERADO: ingrese un nuevo valor\n")

                    while True:
                        try:
                            teléfono=input("Ingrese teléfono de contacto(asegurese que comienze con 09): ")
                            if not teléfono.isdigit():
                                raise ValueError
                            if not teléfono.startswith("09"):
                                raise NoExiste
                            if len(teléfono) != 9:
                                raise FueraDeRango
                            break
                        except ValueError:
                            print("\nERROR: Ingrese un número válido para el teléfono(>0).\n")
                        except FueraDeRango:
                            print("\nError! El teléfono debe tener 9 dígitos\n")
                        except NoExiste:
                            print("\nERROR: El teléfono debe comenzar con 09.\n")
                        except :
                            print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                    while True:
                        try:
                            correo_electrónico= input("ingrese el correo electrónico del cliente: ")
                            if "@" not in correo_electrónico:
                                raise ValueError
                            if correo_electrónico=="":
                                raise ValueError
                            break
                        except ValueError:
                            print("\nERROR: Ingrese un correo válido.\n")
                        except :
                            print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                    print("El cliente fue registrado con éxito!")

                    sistema.registrar_cliente_Empresa(rut, nombre, página_web, teléfono, correo_electrónico)
                    
        
                    
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
                        existencia=0
                        seleccion_cliente = int(input("Ingrese el ID del cliente: "))
                        for cliente in sistema.lista_clientes:
                            if cliente.id == seleccion_cliente:
                                cliente_pedido = cliente
                                existencia=1
                        if existencia==0:
                            raise NoExiste
                        break
                    except ValueError:
                        print("\nERROR: Ingrese un número válido para el ID del cliente.\n")
                    except NoExiste:
                        print("\nERROR: El ID del cliente no existe. Por favor, ingrese un ID válido.\n")
                    except :
                        print("\nERROR INESPERADO: ingrese un nuevo valor\n")

                print("seleccione la máquina que desea registrar un pedido: ")
                sistema.listar_maquinas()
                while True:
                    try:
                        seleccion_maquina = int(input("Ingrese el código de la maquina a registrar: "))
                        encontrar_codigo_maq=0
                        for maquina in sistema.lista_maquinas:
                            if seleccion_maquina == maquina.codigo:
                                encontrar_codigo_maq+=1
                                maquina_pedido = maquina
                        if encontrar_codigo_maq==0:
                            raise NoExiste
                        break
                    except NoExiste:
                        print("\nERROR: El código de la máquina no existe. Por favor, ingrese un código válido.\n")
                        
                    except ValueError:
                        print("\nERROR: Ingrese un número válido para el código de la máquina.\n")
                    except :
                        print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                        
                sistema.registrar_pedido(cliente_pedido,maquina_pedido)
                    
            elif registrar==5:
                if sistema.lista_piezas==[]:
                    print("\nError! No existen piezas para reabastecer\n")
                    break
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
                    except :
                        print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                
                        

                while True:
                    try:
                        cantidad_lotes=int(input("Ingrese la cantidad de lotes a reabastecer: "))
                        if cantidad_lotes<0:
                            raise FueraDeRango
                        break
                    except ValueError:
                        print("\nError! Elija un valor adecuado\n")
                    except FueraDeRango:
                        print("\nError! La cantidad de lotes no puede ser negativa\n")
                    except :
                        print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                sistema.registrar_reposicion(pieza_repuesta,cantidad_lotes)
                print("\nReposicion realizada con exito!\n")
                sistema.completar_pedido()
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
                except :
                    print("\nERROR INESPERADO: ingrese un nuevo valor\n")

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
                        except :
                            print("\nERROR INESPERADO: ingrese un nuevo valor\n")
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
                            except :
                                print("\nERROR INESPERADO: ingrese un nuevo valor\n")
                        sistema.listar_pedidos_filtrados(tipo_pedido)
                    elif filtrado==2:
                        sistema.listar_pedidos()
                    
            elif listar==3:
                    sistema.listar_maquinas()
            elif listar==4:
                    sistema.listar_piezas()
            elif listar==5:
                    sistema.contabilidad()
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
            except :
                print("\nERROR INESPERADO: ingrese un nuevo valor\n")
