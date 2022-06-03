class Drinks:
    """
    Object class model of product, basic items and properties for entry of new items

    
    """
    def __init__(self, id_item:int, name:str,  price: float, description: str, qty: int, in_date: str, out_date: str):
        self.id_item = id_item
        self.name =  name
        self.price = price
        self.description = description
        self.qty = qty
        self.in_date = in_date
        self.out_date = out_date

    def __str__(self) :
        return f"""
        *******************    Producto   *******************
        Name: {self.name}               ID: ´{self.id_item}
        Description: {self.description}
        Price: {self.price}                 Entry Date: {self.id_item}              Expires Date: {self.out_date}
        Qty: {self.qty}                     
"""


    # getters and setter model product
    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, value):
        self.name = value
    
    @property
    def price(self):
        return self.price
    @price.setter
    def price(self, value):
        self.price = value
    
    @property
    def description(self):
        return self.description
    @description.setter
    def description(self, value):
        self.description = value
    
    @property
    def qty(self):
        return self.qty
    @qty.setter
    def qty(self, value):
        self.qty = value
