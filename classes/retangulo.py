class Retangulo:
    def __init__(self, base: float, altura: float):
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, nova_base: float):
        self.__base = nova_base

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, nova_altura: float):
        self.__altura = nova_altura

    def area(self):
        return self.__base * self.__altura

    def perimetro(self):
        return 2 * (self.__base + self.__altura)
