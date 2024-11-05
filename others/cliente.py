class Cliente:
    def __init__(self, nome):
        print("Construindo objeto...{}".format(self))
        self.__nome = nome

    #def get_nome(self):
        #return self.nome.capitalize()

    @property
    def nome(self):
        return self.__nome.capitalize()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome