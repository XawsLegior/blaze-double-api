class perfil:
    def saldo(self):
        response = self.session.request("GET", f"{self.blaze}/api/wallets", headers=self.headers)
        if response.status_code == 200:
            if self.wallet_id is None:
                self.wallet_id = response.json()[0]["id"]
            return response.json()[0]["balance"]
        return None
