class ContaBancaria:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial 

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def get_saldo(self):
        return self._saldo

conta = ContaBancaria(1000)
print("Saldo inicial:", conta.get_saldo())

conta.depositar(500)
print("Novo saldo:", conta.get_saldo())
