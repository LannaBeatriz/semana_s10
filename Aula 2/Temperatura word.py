class SensorTemperatura:
    def __init__(self, temperatura=0):
        self.__temperatura = temperatura  

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, nova_temperatura):
        self.__temperatura = nova_temperatura

sensor = SensorTemperatura(12)
print("Temperatura atual:", sensor.get_temperatura())

nova_temperatura = float(input("Digite a nova temperatura: "))
sensor.set_temperatura(nova_temperatura)

print("Nova temperatura:", sensor.get_temperatura())
