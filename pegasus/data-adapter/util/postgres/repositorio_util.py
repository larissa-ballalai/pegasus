from util.postgres.conexao import ConfiguracoesConexaoPostgresSQL


class RepositorioPostgresSQL:
    def __init__(self, arquivo_configuracao="config.yml"):
        config = ConfiguracoesConexaoPostgresSQL(arquivo_configuracao)
        self.conexao = config.get_conexao()

