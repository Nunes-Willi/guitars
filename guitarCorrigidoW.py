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

class InstrumentType(Enum):
    GUITAR = "Guitar"
    MANDOLIN = "Mandolin"
    SAX = "Sax"
    
class Style(Enum):
    A = "A"
    F = "F"

class Instrument:

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

class InstrumentSpec:

    def __init__(self, properties):
        self.properties = properties

    def getProperty(self, propertyName):
        return self.properties.get(propertyName)

    def getProperties(self):
        return self.properties

    def matches(self, otherSpec):

        for prop in otherSpec.getProperties():

            if self.properties.get(prop) != otherSpec.getProperty(prop):
                return False

        return True

class Inventory:

    def __init__(self):
        self.instruments = []

    def addInstrument(self, serialNumber, price, spec):

        self.instruments.append(
            Instrument(serialNumber, price, spec)
        )

    def search(self, searchSpec):

        matching = []

        for instrument in self.instruments:

            if instrument.getSpec().matches(searchSpec):
                matching.append(instrument)

        return matching

def initializeInventory(inventory):
    inventory.addInstrument(
    "V95693",
    1499.95,
    InstrumentSpec({
        "instrumentType": InstrumentType.GUITAR.value,
        "builder": Builder.FENDER.value,
        "model": "Stratocaster",
        "type": Type.ELECTRIC.value,
        "backWood": Wood.ALDER.value,
        "topWood": Wood.ALDER.value,
        "numStrings": 6
    })
)
    inventory.addInstrument(
    "M12345",
    2499.95,
    InstrumentSpec({
        "instrumentType": InstrumentType.MANDOLIN.value,
        "builder": Builder.GIBSON.value,
        "model": "F5-G",
        "type": Type.ACOUSTIC.value,
        "backWood": Wood.MAHOGANY.value,
        "topWood": Wood.MAPLE.value,
        "style": Style.F.value
    })
)
    inventory.addInstrument(
    "SX1001",
    3299.90,
    InstrumentSpec({
        "instrumentType": InstrumentType.SAX.value,
        "builder": Builder.GIBSON.value,
        "model": "YAS-280",
        "finish": "Gold Lacquer",
        "key": "Eb"
    })
)

def main():

    inventory = Inventory()
    initializeInventory(inventory)

    searchMandolin = InstrumentSpec({
        "instrumentType": InstrumentType.MANDOLIN.value,
        "builder": Builder.GIBSON.value,
        "model": "F5-G"
    })

    resultado = inventory.search(searchMandolin)

    print("Mandolins encontradas:")

    for instrumento in resultado:
        print(
            f"{instrumento.getSerialNumber()} "
            f"- US${instrumento.getPrice():.2f}"
        )

    whatErinLikes = InstrumentSpec({
        "instrumentType": InstrumentType.GUITAR.value,
        "builder": Builder.FENDER.value,
        "model": "Stratocaster"
    })

    matchingGuitars = inventory.search(whatErinLikes)

    if matchingGuitars:

        print("\nErin, talvez você goste destas guitarras:")

        for instrument in matchingGuitars:

            spec = instrument.getSpec()

            print(
                f"\nSerial: {instrument.getSerialNumber()}"
                f"\nBuilder: {spec.getProperty('builder')}"
                f"\nModelo: {spec.getProperty('model')}"
                f"\nTipo: {spec.getProperty('type')}"
                f"\nMadeira traseira: {spec.getProperty('backWood')}"
                f"\nMadeira tampo: {spec.getProperty('topWood')}"
                f"\nCordas: {spec.getProperty('numStrings')}"
                f"\nPreço: US${instrument.getPrice():.2f}"
            )

    else:
        print("Desculpe Erin, não temos nada para você")

    searchSax = InstrumentSpec({
        "instrumentType": InstrumentType.SAX.value,
        "key": "Eb"
    })

    saxes = inventory.search(searchSax)

    print("\nSaxofones encontrados:")

    for instrument in saxes:

        spec = instrument.getSpec()

        print(
            f"\nSerial: {instrument.getSerialNumber()}"
            f"\nModelo: {spec.getProperty('model')}"
            f"\nAcabamento: {spec.getProperty('finish')}"
            f"\nTom: {spec.getProperty('key')}"
            f"\nPreço: US${instrument.getPrice():.2f}"
        )

if __name__ == "__main__":
    main()