from enum import Enum

class builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"

class model(Enum):
    STRATOCASTER = "stratocaster"
    TELECASTER = "telecaster"
    LES_PAUL = "les_paul"
    SG = "sg"
    FLYING_V = "flying_v"
    EXPLORER = "explorer"
    JAZZMASTER = "jazzmaster"
    HOLLOWBODY = "hollowbody"

class typeG(Enum):
    ACOUSTIC = "acoustic"
    ELETRIC = "eletric"

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

class Guitar:
    def __init__(self, serialNumber, price, builder, model, typeG, backWood, topWood):
        self.serialNumber = serialNumber
        self.price = price
        self.builder = builder #
        self.model = model #
        self.typeG = typeG #
        self.backWood = backWood ##
        self.topWood = topWood ##

    def getSerialNumber(self):
        return self.serialNumber

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice

    def getBuilder(self):
        return self.builder

    def getModel(self):
        return self.model

    def getTypeG(self):
        return self.typeG

    def getBackWood(self):
        return self.backWood

    def getTopWood(self):
        return self.topWood

class Inventory:
    def __init__(self):
        self.guitars = []

    def addGuitar(self, serialNumber, price, builder, model, typeG, backWood, topWood):
        guitar = Guitar(serialNumber, price, builder, model, typeG, backWood, topWood)
        self.guitars.append(guitar)

    def getGuitar(self, serialNumber):
        for guitar in self.guitars:
            if guitar.getSerialNumber() == serialNumber:
                return guitar
        return None

    def searchGuitar(self, searchGuitar):
        for guitar in self.guitars:
            builder = searchGuitar.getBuilder()
            if builder is not None and builder != "" and builder != guitar.getBuilder():
                continue
            model = searchGuitar.getModel()
            if model is not None and model != "" and model != guitar.getModel():
                continue
            typeG = searchGuitar.getTypeG()
            if typeG is not None and typeG != "" and typeG != guitar.getTypeG():
                continue
            backWood = searchGuitar.getBackWood()
            if backWood is not None and backWood != "" and backWood != guitar.getBackWood():
                continue
            topWood = searchGuitar.getTopWood()
            if topWood is not None and topWood != "" and topWood != guitar.getTopWood():
                continue
            return guitar
        return None

inventory = Inventory()

inventory.addGuitar("V95693", 1499.95, "Fender", "Stratocastor", "electric", "Alder", "Alder")
#inventory.addGuitar("11277", 3999.95, "Collings", "CJ", "acoustic", "Indian Rosewood", "Indian Rosewood")


whatErinLikes1 = Guitar("", 0, "fender", "Stratocastor", "electric", "Alder", "Alder")

guitar = inventory.searchGuitar(whatErinLikes1)
if guitar:
    print(f"Erin, you might like this {guitar.getBuilder()} {guitar.getModel()} {guitar.getTypeG()} guitar:\n{guitar.getBackWood()} back and sides,\n{guitar.getTopWood()} top.\nYou can have it for only ${guitar.getPrice()}!")
else:
    print("Sorry, Erin, we have nothing for you.")


#print("\n")
# Buscando outra guitarra que o Erin gosta no estoque
#whatErinLikes2 = Guitar("11277", 3999.95, "Collings", "CJ", "acoustic", "Indian Rosewood", "Indian Rosewood")

#guitar = inventory.searchGuitar(whatErinLikes2)
#if guitar:
#    print(f"Erin, you might like this {guitar.getBuilder()} {guitar.getModel()} {guitar.getTypeG()} guitar:\n{guitar.getBackWood()} back and sides,\n{guitar.getTopWood()} top.\nYou can have it for only ${guitar.getPrice()}!")
#else:
#    print("Sorry, Erin, we have nothing for you.")

# Testando o Sistema

# Set up Rick’s guitar inventory
inventory = Inventory()

# Adiciona guitarras ao estoque
inventory.addGuitar("V95693", 1499.95, "Fender", "Stratocastor", "electric", "Alder", "Alder")
#inventory.addGuitar("11277", 3999.95, "Collings", "CJ", "acoustic", "Indian Rosewood", "Indian Rosewood")


# Buscando por uma guitarra que o Erin gosta: Fender Stratocastor elétrica com corpo de Alder e tampo de Alder
whatErinLikes1 = Guitar("", 0, "fender", "Stratocastor", "electric", "Alder", "Alder")

guitar = inventory.searchGuitar(whatErinLikes1)
if guitar:
    print(f"Erin, you might like this {guitar.getBuilder()} {guitar.getModel()} {guitar.getTypeG()} guitar:\n{guitar.getBackWood()} back and sides,\n{guitar.getTopWood()} top.\nYou can have it for only ${guitar.getPrice()}!")
else:
    print("Sorry, Erin, we have nothing for you.")