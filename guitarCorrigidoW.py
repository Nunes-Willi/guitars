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

class GuitarSpec:
    def __init__(self, builder, model, typeG,
                 backWood, topWood, numStrings):

        self.builder = builder
        self.model = model
        self.typeG = typeG
        self.backWood = backWood
        self.topWood = topWood
        self.numStrings = numStrings

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

    def getNumStrings(self):
        return self.numStrings

    def matches(self, otherSpec):

        if self.builder != otherSpec.getBuilder():
            return False

        if str(self.model).lower() != str(otherSpec.getModel()).lower():
            return False

        if self.typeG != otherSpec.getTypeG():
            return False

        if self.backWood != otherSpec.getBackWood():
            return False

        if self.topWood != otherSpec.getTopWood():
            return False

        if self.numStrings != otherSpec.getNumStrings():
            return False

        return True

class Guitar:
    def __init__(self, serialNumber, price, spec):
        self.serialNumber = serialNumber
        self.price = price
        self.spec = spec

    def getSerialNumber(self):
        return self.serialNumber

    def getPrice(self):
        return self.price

    def getSpec(self):
        return self.spec

class Style(Enum):
    A = "A"
    F = "F"


class MandolinSpec:
    def __init__(self, builder, model, typeG,
                 backWood, topWood, style):

        self.builder = builder
        self.model = model
        self.typeG = typeG
        self.backWood = backWood
        self.topWood = topWood
        self.style = style

    def matches(self, otherSpec):
        return (
            self.builder == otherSpec.builder and
            self.model == otherSpec.model and
            self.typeG == otherSpec.typeG and
            self.backWood == otherSpec.backWood and
            self.topWood == otherSpec.topWood and
            self.style == otherSpec.style
        )


class Mandolin:
    def __init__(self, serialNumber, price, spec):
        self.serialNumber = serialNumber
        self.price = price
        self.spec = spec

    def getSerialNumber(self):
        return self.serialNumber

    def getPrice(self):
        return self.price

    def getSpec(self):
        return self.spec


class Inventory:
    def __init__(self):
        self.guitars = []
        self.mandolins = []

    def addGuitar(self, serialNumber, price, spec):
        self.guitars.append(
            Guitar(serialNumber, price, spec)
        )

    def addMandolin(self, serialNumber, price, spec):
        self.mandolins.append(
            Mandolin(serialNumber, price, spec)
        )

    def searchGuitar(self, searchSpec):
        result = []

        for guitar in self.guitars:
            if guitar.getSpec().matches(searchSpec):
                result.append(guitar)

        return result

    def searchMandolin(self, searchSpec):
        result = []

        for mandolin in self.mandolins:
            if mandolin.getSpec().matches(searchSpec):
                result.append(mandolin)

        return result


def initializeInventory(inventory):

    spec1 = GuitarSpec(
        Builder.FENDER,
        "stratocastor",
        Type.ELECTRIC,
        Wood.ALDER,
        Wood.ALDER,
        6
    )
    mandolinSpec = MandolinSpec(
        Builder.GIBSON,
        "F5-G",
        Type.ACOUSTIC,
        Wood.MAHOGANY,
        Wood.MAPLE,
        Style.F
    )

    inventory.addGuitar("V95693", 1499.95, spec1)
    inventory.addGuitar("V99999", 1599.95, spec1)
    inventory.addMandolin("M12345",2499.95,mandolinSpec)

def main():

    inventory = Inventory()
    initializeInventory(inventory)

    searchSpec = MandolinSpec(
        Builder.GIBSON,
        "F5-G",
        Type.ACOUSTIC,
        Wood.MAHOGANY,
        Wood.MAPLE,
        Style.F
    )

    resultado = inventory.searchMandolin(searchSpec)

    print("Mandolins encontradas:")

    for mandolin in resultado:
        print(
            f"{mandolin.getSerialNumber()} "
            f"- US${mandolin.getPrice():.2f}"
        )

    whatErinLikes = GuitarSpec(
        Builder.FENDER,
        "Stratocastor",
        Type.ELECTRIC,
        Wood.ALDER,
        Wood.ALDER,
        6
    )
    matchingGuitars = inventory.searchGuitar(whatErinLikes)

    if matchingGuitars:

        print("Erin, talvez você goste destas:")

        for guitar in matchingGuitars:

            guitarSpec = guitar.getSpec()

            print(
                f"\nGuitarra: {guitar.getSerialNumber()} "
                f"{guitarSpec.getBuilder().value} "
                f"{guitarSpec.getModel()} "
                f"{guitarSpec.getTypeG().value}\n"
                f"{guitarSpec.getBackWood().value} na traseira e laterais,\n"
                f"{guitarSpec.getTopWood().value} no tampo,\n"
                f"com {guitarSpec.getNumStrings()} cordas\n"
                f"Ela pode ser sua por apenas "
                f"US${guitar.getPrice():.2f}!"
            )

    else:
        print("Desculpe Erin, não temos nada para você")


if __name__ == "__main__":
    main()