class Supplies:
    def __init__(self, nombre:str, cantidad:float, descripcion:str, ingreso:str, costo:float,currency:str,type_cant:str, id_supplie:int= None,  img:str= None, salida:str= None):
        self._name = nombre
        self._qty = cantidad
        self._description = descripcion
        self._incoming = ingreso
        self._price = costo
        self._currency = currency
        self._out = salida
        self._id_num = id_supplie
        self._size = type_cant
        self._image = img

    def __str__(self):
        return f"""
    Imagen: {self.prod_img}
    Producto: {self.name}
    No. ID: {self.id_num}
    Inventario: {self.qty} {self.size}
    Precio: ${self.price} {self.currency}
    Ingreso: {self.incoming}
    Salida: {self.out}
    Descripcion:
        {self.description}
    """

    @property
    def prod_img(self):
        return self._image
    @prod_img.setter
    def prod_img(self, new_url):
        self._image = new_url

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def id_num(self):
        return self._id_num
    @id_num.setter
    def id_num(self, new_id):
        self._id_num = new_id

    @property
    def qty(self):
        return self._qty
    @qty.setter
    def qty(self, new_qty):
        self._qty = new_qty

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, new_size):
        self._size = new_size

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        self._price = new_price

    @property
    def currency(self):
        return self._currency
    @currency.setter
    def currency(self, new_currency):
        self._currency = new_currency

    @property
    def incoming(self):
        return self._incoming
    @incoming.setter
    def incoming(self, new_incoming):
        self.incoming = new_incoming

    @property
    def out(self):
        return self._out
    @out.setter
    def out(self, new_out):
        self._out = new_out

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, new_description):
        self._description = new_description

if __name__ == "__main__":
    product = Supplies("Pepsi", 12, "Bebida carbonatada sabor cola", "12/03/2021", 17.67,"MXN", "pzs", 123)
    print(product)