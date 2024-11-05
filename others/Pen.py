# created Caneta class with their attributes (color, brand etc.)
# and methods that represents pens behaviors like write, cap and uncap

class Pen:
    # Initializes a Caneta instance with color, brand, charge, and capped status
    def __init__(self, color, brand, charge, capped):
        self.color = str(color)
        self.brand = str(brand)
        self.charge = int(charge)
        self.capped = capped

    # Writes with the pen if uncapped, prompts to uncap otherwise
    def write(self):
        if not self.capped:
            print('A caneta está escrevendo...')
        else:
            print('Retire a tampa da caneta antes de começar a escrever!')

    # Caps the pen, preventing it from writing
    def cap(self):
        self.capped = True
        print('A caneta foi tampada.')

    # Uncaps the pen, allowing it to write
    def uncap(self):
        self.capped = False
        print('A caneta foi destampada.')

    def get_color(self):
        print(self.color)