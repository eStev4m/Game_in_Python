class Cachorros:
    def __init__(self, nome, cor_de_pelo, idade, tamanho):
        self.nome = nome
        self.cor_de_pelo = cor_de_pelo
        self.idade = idade
        self.tamanho = tamanho


    def latir(self):
        print(f'\033[1;31mAu Au\033[m é como o \033[1;34m{self.nome}\033[m faz.')

    
    def correr(self):
        print(f'\033[1;34m{self.nome}\033[m esta correndo.')
