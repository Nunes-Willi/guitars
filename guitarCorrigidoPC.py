# Observe que em Python usamos a classe "Enum" do módulo "enum" em vez de "enumeração"
# "Enum" é um tipo de dados embutido em Python. É usado para criar um conjunto finito de constantes.
# "Enum" é uma coleção de nomes e valores simbólicos. É um atalho para enumeração e pode ser importado do módulo "enum"
# Uma das grandes vantagens de usar "enums" é que ele limita os possíveis valores
# que você pode fornecer a um método... sem mais erros ortográficos ou problemas de maiúsculas e minúsculas
from enum import Enum

# Podemos nos referir a eles como Wood.SITKA ou Builder.GIBSON
# e evitar todas essas comparações de strings completamente
class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"

#Cada "enum" toma o lugar de uma das propriedades de uma guitarra
class TypeG(Enum):
    ACOUSTIC = "acoustic"
    ELETRIC = "eletric"


# Podemos nos referir a eles como Wood.SITKA ou Builder.GIBSON 
# e evitar todas essas comparações de strings completamente
class Wood(Enum):
    INDIAN_ROSEWOOD = "indian_rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian_rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "ococobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"

#Classe Guitar
class Guitar:
    def __init__(self, serial_number, price, builder, model, typeg, back_wood, top_wood):
        self.serial_number = serial_number
        self.price = price
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.back_wood = back_wood
        self.top_wood = top_wood

    def get_serial_number(self):
        return self.serial_number

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def get_builder(self):
        return self.builder

    def get_typeg(self):
        return self.typeg

    def get_model(self):
        return self.model

    def get_back_wood(self):
        return self.back_wood

    def get_top_wood(self):
        return self.top_wood
#Classe Inventory
class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, serial_number, price, builder, model, typeg, back_wood, top_wood):
        guitar = Guitar(serial_number, price, builder, model, typeg, back_wood, top_wood)
        self.guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in self.guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar
        return None

    def search_guitar(self, search_guitar):
        for guitar in self.guitars:
            # Parece que nada mudou, mas com "Enums", não precisamos nos preocupar com essas comparações 
            # sendo prejudicadas por erros ortográficos ou problemas de maiúscula/minúscula
            if search_guitar.get_builder() != guitar.get_builder():
                continue

            # A única propriedade com a qual precisamos nos preocupar é o "model", já que ainda é uma String
            model = search_guitar.get_model().lower()
            if model and model != "" and model != guitar.get_model().lower():
                continue

            # Parece que nada mudou, mas com "Enums", não precisamos nos preocupar com essas comparações 
            # sendo prejudicadas por erros ortográficos ou problemas de maiúscula/minúscula
            if search_guitar.get_typeg() != guitar.get_typeg():
                continue
            if search_guitar.get_back_wood() != guitar.get_back_wood():
                continue
            if search_guitar.get_top_wood() != guitar.get_top_wood():
                continue
            return guitar
        return None

# Testando o Sistema

# Set up Rick’s guitar inventory
inventory = Inventory()

# Adiciona guitarras ao estoque
inventory.add_guitar("V95693", 1499.95, Builder.FENDER.value, "Stratocastor", TypeG.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)
#inventory.add_guitar("11277", 3999.95, Builder.COLLINGS.value, "Stratocastor", TypeG.ACOUSTIC.value, Wood.INDIAN_ROSEWOOD.value, Wood.INDIAN_ROSEWOOD.value)


# Buscando por uma guitarra que o Erin gosta: Fender Stratocastor elétrica com corpo de Alder e tampo de Alder
whatErinLikes = Guitar(" ", 0, Builder.FENDER.value, "Stratocastor", TypeG.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)
guitar = inventory.search_guitar(whatErinLikes)
if guitar is not None:
  print(f"Erin, talvez você goste desta: {guitar.get_builder()} {guitar.get_model()} {guitar.get_typeg()} guitar:\n {guitar.get_back_wood()} na traseira e laterais, \n{guitar.get_top_wood()} no tampo.\n Ela pode ser sua por apenas US${guitar.get_price()}!")
else:
  print("Desculpe Erin, não temos nada para você")