# Intro to programming
# Classes and Objects
# Phan Viet Anh
# 256296


class CellPhone:

    def __init__(self, manufact, model, retail_price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = retail_price

    def set_manufact(self, manufact):
        self.__manufact = manufact

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, retail):
        self.__retail_price = retail

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return  self.__model

    def get_retail(self):
        return self.__retail_price

    def __str__(self):
        return 'The state of your Phone now is ' + self.get_manufact() \
               + ', ' + self.get_model() + ', ' + format(self.get_retail(), '.2f')


