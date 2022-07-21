from Modules.prod_module import Supplies

# Se agrega la clase para el manejo de items, CRUD.
class ManagerItem:

    def __init__(self, producto:Supplies):
        self._producto = producto


    @classmethod
    def add_item(cls):
        no