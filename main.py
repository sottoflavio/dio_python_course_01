import datetime

class SistemaBancario:
    
    def __init__(self):
        self.saldo = 0
        self.limite_diario = 1500
        self.numero_saque = 0
        self.ultima_data_saque = None
        self.saques = []
        self.depositos = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
        else:
            print(f'O Valor do depósito não pode ser negativo ou nulo')
        print(f'Depósito de R${valor} realizado. Novo saldo: R${self.saldo}')

    def saque(self, valor):
        hoje = datetime.date.today()

        if self.ultima_data_saque != hoje:
            self.limite_diario = 1500
            self.ultima_data_saque = hoje
            self.numero_saque = 0

        if valor <= self.saldo and valor <= self.limite_diario and self.numero_saque < 3 and valor < 500: 
            self.saldo -= valor
            self.limite_diario -= valor
            self.numero_saque += 1
            self.saques.append(valor)
            print(f'Saque de R${valor} realizado. Novo saldo: R${self.saldo}')
        elif valor > self.limite_diario:
            print('Limite diário de saque excedido. Máximo permitido: R$1500')
        elif valor > 500:
            print('Limite máximo por saque de R$ 500,00')
        elif valor > self.saldo:
            print('Saldo indisponível')
        else:
            print('Máximo de 3 saques por dia excedidos.')

    def extrato(self):
        print(f'Saldo atual: R${self.saldo:.2f}')
        print(f'Depósitos: {[f"R$ {deposito:.2f}" for deposito in self.depositos]}')
        print(f'Saques: {[f"R$ {saque:.2f}" for saque in self.saques]}')


def main():
    sistema_bancario = SistemaBancario()
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("0. Sair")

        escolha = int(input("Digite o número da opção desejada: "))

        if escolha == 1:
            valor_deposito = float(input("Digite o valor do depósito: "))
            sistema_bancario.deposito(valor_deposito)
        elif escolha == 2:
            valor_saque = float(input("Digite o valor do saque: "))
            sistema_bancario.saque(valor_saque)
        elif escolha == 3:
            sistema_bancario.extrato()
        elif escolha == 0:
            print("Sistema encerrado. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
