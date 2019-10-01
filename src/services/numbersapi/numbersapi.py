from src.core.service import Service


class Numbersapi(Service):
    def __init__(self):
        super().__init__()
        self._set_hostname('https://numbersapi.p.rapidapi.com')
        self._set_header('x-rapidapi-key', '09ed993a15msh5f0945b56a7f408p1224c4jsn49cbc7efc09f')
