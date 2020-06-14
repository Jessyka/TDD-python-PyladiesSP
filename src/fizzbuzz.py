class FizzBuzz():
    def converter(self, numero):
        saida = ''

        if self.eh_multiplo_de_3(numero):
            saida += 'fizz'
        if self.eh_multiplo_de_5(numero):
            saida += 'buzz'
        if saida == '':
            saida += str(numero)
        return saida

    def eh_multiplo_de_3(self, numero):
        return numero % 3 == 0

    def eh_multiplo_de_5(self, numero):
        return numero % 5 == 0