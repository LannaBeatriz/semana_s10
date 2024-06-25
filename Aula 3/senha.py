class Usuario:
    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha

    def alterar_senha(self, nova_senha):
        if self.__verificar_seguranca_senha(nova_senha):
            self.__senha = nova_senha
            print("Senha alterada com sucesso!")
        else:
            print("A nova senha não atende aos critérios de segurança.")

    def __verificar_seguranca_senha(self, senha):
        tamanho_minimo = 6
        if len(senha) >= tamanho_minimo:
            return True
        else:
            return False

    def get_nome(self):
        return self.__nome

    def get_senha(self):
        return self.__senha

usuario1 = Usuario("fulano", "senhaAntiga123")
print("Senha atual:", usuario1.get_senha())
usuario1.alterar_senha("nova")
usuario1.alterar_senha("novaSenhaSegura123")
usuario1.__nome("Nome de usuario")
print("Nova senha:", usuario1.get_senha())
