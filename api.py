import requests
from API.login import *
from API.perfil import *
from API.jogo import *

class api:

    """ PEGA HORA DIRETO DA BLAZE
    FORMATO RETORNADO (DICT, INT)
    {"hora": 10, "minuto": 22}
    """
    def getTime(self):
        return jogo.getTime(self)

    """ FAZER LOGIN """
    def login(self, usuario, senha):
        return login.entrar(self, usuario, senha)

    """ PEGAR SALDO """
    def getSaldo(self):
        return perfil.saldo(self)

    """ PEGAR STATUS ATUAL DA ROLETA """
    """ WAITING/COMPLETE/ROLLING """
    def getStatus(self):
        try:
            return jogo.getStatus(self)
        except Exception as e:
            print(e)

    """ PEGAR ÚLTIMO(S) X RESULTADOS """
    def getResultado(self):
        try:
            return jogo.getResultado(self)
        except Exception as e:
            print("resultado-->",e)

    def entrada(self, valor, api, **cor):
        try:
            return jogo.entrada(self, valor, api, cor=cor)
        except Exception as e:
            print(e)

    def __init__(self):
        self.blaze = "https://blaze1.space"
        self.conectado = False
        self.response = "Não conectado!"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0"
        }
        self.wallet_id = None
        self.session = requests.Session()
