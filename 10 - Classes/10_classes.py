import uuid


class GerenciamentoUsuarios:
    def __init__(self, email: str, senha: str) -> None:
        self.email = email
        self.senha = senha
        self.usuarios = [
            {
                'id': 1,
                'email': 'teste.teste@test-mail.com',
                'senha': 'teste'
            },
            {
                'id': 2,
                'email': 'nome.sobrenome@some-email.com',
                'senha': '123456'
            }
        ]
        self.token = None
    
    @staticmethod
    def gerar_token() -> str:
        return str(uuid.uuid4())
    
    def realizar_login(self) -> bool:
        for usuario in self.usuarios:
            if usuario['email'] == self.email and usuario['senha'] == self.senha:
                self.token = self.gerar_token()
                return True
        return False
    
    def realizar_logout(self) -> None:
        self.token = None
        return None


class Sistema(GerenciamentoUsuarios):
    def __init__(self, email: str, senha: str) -> None:
        super().__init__(email, senha)
    
    