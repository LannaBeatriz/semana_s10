class Veiculo:
    def acelerar(self):
        raise NotImplementedError("Método acelerar deve ser implementado.")

class Carro(Veiculo):
    def acelerar(self):
        print("Carro acelerando.")

class Motocicleta(Veiculo):
    def acelerar(self):
        print("Motocicleta acelerando.")

# Exemplo de uso:
carro = Carro()
carro.acelerar()  # Deve imprimir "Carro acelerando."

moto = Motocicleta()
moto.acelerar()  # Deve imprimir "Motocicleta acelerando."