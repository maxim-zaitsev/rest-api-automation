from src.core.service import Service


class Reqres(Service):
    def __init__(self):
        super().__init__()
        self._set_hostname('http://reqres.in')
