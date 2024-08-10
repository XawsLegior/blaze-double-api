from datetime import datetime
from threading import Thread
import requests


class jogo:
    main_parent = None
    blaze = None
    headers = None
    session = None

    """ PEGA HORA DIRETO DA BLAZE """
    def getTime(self):
        hora = self.session.request("GET", f"{self.blaze}/api/roulette_games/current", headers=self.headers).json()["updated_at"].replace("Z", "+00:00")
        dataHM = datetime.strftime(datetime.fromisoformat(hora), "%H:%M").split(":")
        return {"hora": int(dataHM[0]), "minuto": int(dataHM[1])}

    """ PEGAR DADOS DA JOGADA """
    def getStatus(self):
        try:
            return self.session.request("GET", f"{self.blaze}/api/roulette_games/current").json()["status"]
        except Exception as e:
            print(e)

    def getResultado(self):
        try:
            result = self.session.request("GET", f"{self.blaze}/api/roulette_games/recent").json()[0]
            cor_result = result["color"]
            cor = "branco"
            if cor_result == 1:
                cor = "vermelho"
            elif cor_result == 2:
                cor = "preto"

            data = result["created_at"].replace("Z", "+00:00")
            dataHM = datetime.strftime(datetime.fromisoformat(data), "%H:%M").split(":")
            dado = {
                "cor": cor,
                "numero": result["roll"],
                "minuto": int(dataHM[1])
            }
            return dado
        except Exception as e:
            print(e)

    """ FAZER ENTRADA                                                      """
    """ se a variável 'cor' receber valor ela vai entrar na cor informada  """
    """ caso contrário entra sempre no branco                              """
    def entrada(self, valor, API, **cor):
            try:
                cor = cor["cor"]["cor"]
                data = {
                    "amount": valor,
                    "currency_type": "BRL",
                    "color": cor,
                    "free_bet": False,
                    "wallet_id": API.wallet_id
                }
            except:
                data = {
                    "amount": valor,
                    "currency_type": "BRL",
                    "color": 0,
                    "free_bet": False,
                    "wallet_id": API.wallet_id
                }

            response = API.session.request("POST", f"{API.blaze}/api/roulette_bets", json=data, headers=API.headers)
            result = {
                "status_code": response.status_code,
                "text": response.text
            }
            return result
