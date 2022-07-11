from datetime import datetime

class Supplies:
    def __init__(self, nombre:str, cantidad:float, descripcion:str, ingreso:str, costo:float, salida:str, id_supplie:int, type_cant:str):
        self.name = nombre
        self.qty = cantidad
        self.desc = descripcion
        self.incoming = ingreso
        self.price = costo
        self.out = salida
        self.id_num = id_supplie
        self.size = type_cant


    def in_date(self):
        date_now = datetime.now()
        formating = date_now.strftime("%D/%m/%Y")



if __name__ == "__name__":
    product = Supplies("Pepsi", 12, "Bebida carbonatada", "12-03-2021", 17.67, None, 1, "pzs")
    product.in_date()