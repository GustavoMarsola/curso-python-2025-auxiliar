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


class SistemaPedidos(GerenciamentoUsuarios):
    def __init__(self, email: str, senha: str) -> None:
        super().__init__(email, senha)
        self.pedidos = []
    
    def realizar_pedido(self, pedido: dict) -> None:
        if self.token:
            self.pedidos.append(pedido)
        return None
    
    def listar_pedidos(self) -> list:
        if self.token:
            return self.pedidos
        return []
    
    def excluir_pedido(self, id_pedido: int) -> None:
        if self.token:
            for pedido in self.pedidos:
                if pedido['id'] == id_pedido:
                    self.pedidos.remove(pedido)
        return None

