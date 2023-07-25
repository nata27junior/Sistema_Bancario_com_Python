class Banco:
    def __init__(self):
        self.saldo = 0

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de {valor} realizado. Saldo atual: {self.saldo}')
        else:
            print('O valor do depósito deve ser maior que zero.')

    def saque(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de {valor} realizado. Saldo atual: {self.saldo}')
            else:
                print('Saldo insuficiente.')
        else:
            print('O valor do saque deve ser maior que zero.')

    def extrato(self):
        print(f'Saldo atual: {self.saldo}')


# Exemplo de uso do sistema bancário
banco = Banco()

banco.deposito(100)  # Depósito de 100 realizado. Saldo atual: 100
banco.saque(50)     # Saque de 50 realizado. Saldo atual: 50
banco.extrato()     # Saldo atual: 50
