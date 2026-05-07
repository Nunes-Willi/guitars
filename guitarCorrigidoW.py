from enum import Enum

class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    ANY = "any"

class Model(Enum):
    STRATOCASTER = "stratocaster"
    TELECASTER = "telecaster"
    LES_PAUL = "les_paul"


class Type(Enum):
    ACOUSTIC = "acoustic"
    ELECTRIC = "electric"

class Wood(Enum):
    ALDER = "alder"
    MAHOGANY = "mahogany"
    MAPLE = "maple"

class Guitar:
    def __init__(self, serialNumber, price, builder, model, typeG, backWood, topWood):
        self.serialNumber = serialNumber
        self.price = price
        self.builder = builder
        self.model = model
        self.typeG = typeG
        self.backWood = backWood
        self.topWood = topWood


class GuitarSpec:
    def __init__(self, builder=None, model=None, typeG=None, backWood=None, topWood=None):
        self.builder = builder
        self.model = model
        self.typeG = typeG
        self.backWood = backWood
        self.topWood = topWood

    def matches(self, otherSpec):
        if self.builder and self.builder != otherSpec.builder:
            return False
        if self.model and self.model != otherSpec.model:
            return False
        if self.typeG and self.typeG != otherSpec.typeG:
            return False
        if self.backWood and self.backWood != otherSpec.backWood:
            return False
        if self.topWood and self.topWood != otherSpec.topWood:
            return False
        return True


class Inventory:
    def __init__(self):
        self.guitars = []

    def addGuitar(self, serialNumber, price, spec):
        self.guitars.append(Guitar(serialNumber, price, **spec.__dict__))

    def search(self, searchSpec):
        matching = []
        for guitar in self.guitars:
            guitarSpec = GuitarSpec(
                guitar.builder,
                guitar.model,
                guitar.typeG,
                guitar.backWood,
                guitar.topWood
            )

            if searchSpec.matches(guitarSpec):
                matching.append(guitar)

        return matching


# ---------------- TESTE ----------------

inventory = Inventory()

inventory.addGuitar(
    "V95693",
    1499.95,
    GuitarSpec(
        Builder.FENDER,
        Model.STRATOCASTER,
        Type.ELECTRIC,
        Wood.ALDER,
        Wood.ALDER
    )
)

searchSpec = GuitarSpec(
    Builder.FENDER,
    Model.STRATOCASTER,
    Type.ELECTRIC,
    Wood.ALDER,
    Wood.ALDER
)

results = inventory.search(searchSpec)

if results:
    for guitar in results:
        print(f"Você pode gostar dessa guitarra:")
        print(f"{guitar.builder.value} {guitar.model.value}")
        print(f"${guitar.price}\n")
else:
    print("Nada encontrado.")