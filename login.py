class login:
    def entrar(self, usuario, senha):
        data = {
            "username": usuario,
            "password": senha
        }

        self.headers["x-captcha-response"] = None
        self.headers["referer"] = f"{self.blaze}/pt/?modal=auth&tab=login"
        response = self.session.request("PUT", f"{self.blaze}/api/auth/password", json=data, headers=self.headers)
        if not response.json().get("error"):
            self.headers["authorization"] = f"Bearer {response.json()["access_token"]}"
            self.conectado = True
            return
        self.response = response.json()
        return self.response