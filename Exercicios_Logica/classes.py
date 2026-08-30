#Agregada

class Fone:
    def __init__(self,marca):
        self.marca = marca

class Celular:
    def __init__(self,modelo):
        self.modelo = modelo
        self.fone = None

meu_fone = Fone('JBL')
meu_celular = Celular('Iphone')
meu_celular.fone = meu_fone

#Composta

class Fonec:
    def __init__(self,marca):
        self.marca = marca

class Celularc:
    def __init__(self,modelo,marca_fone):
        self.modelo = modelo
        self.fone = Fonec(marca_fone)