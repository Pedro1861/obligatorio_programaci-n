from datetime import datetime

class Pedido:
    def __init__(self, cliente, maquina, fecha_recibido, fecha_entregado, estado, precio):
        self.cliente = cliente
        self.maquina = maquina
        self.fecha_recibido = fecha_recibido
        self.fecha_entregado = fecha_entregado
        self.estado = estado
        self.precio = precio
    
    # NO SE COMO HACER PARA SEPARAR CLIENTE INDIVIDUAL DE EMPRESA, 
    # PORQUE SI ES INDIVIDUAL ES COSTO DE VENTA * 1.5 (EL COSTO DE VENTA +50%) 
    # Y SI ES EMPRESA ES EL PRECIO (COSTO DE VENTA * 1.5) * 0.8 
    # QUE SERIA EL 20% DE DESCUENTO POR SER EMPRESA
     
    def get_precio(self):
        return self.precio
    
    
        
