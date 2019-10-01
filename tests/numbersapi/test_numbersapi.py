from src.services.numbersapi.numbersapi import Numbersapi


class TestNumbersapi:
    def test_get_date_fact(self):
        napi = Numbersapi()
        r, d = napi.get('/6/21/date')
        napi.verify(r.status_code == 200)
        napi.verify(d.startswith('June 21st'))
        napi.is_failed()
