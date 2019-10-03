from src.services.numbersapi.numbersapi import Numbersapi


class TestNumbersapi:
    def test_get_date_fact_plain_text(self):
        napi = Numbersapi()
        napi.get_request_params().clear()
        r, d = napi.get('/6/21/date')
        napi.verify(r.status_code, 200)
        napi.verify(d.startswith('June 21st'))
        napi.is_failed()

    def test_get_date_fact(self):
        napi = Numbersapi()
        r, d = napi.get('/6/21/date')
        napi.verify(r.status_code, 200)
        napi.verify('application/json' in r.headers['content-type'])
        napi.verify(d['text'])
        napi.verify(d['type'], 'date')
        napi.verify(str(d['year'] ** 1) in d['text'])
        napi.is_failed()

    def test_get_math_fact(self):
        napi = Numbersapi()
        r, d = napi.get('/2/math')
        napi.verify(r.status_code, 200)
        napi.verify(d['text'])
        napi.verify(d['number'], 2)
        napi.verify(d['type'], 'math')
        napi.is_failed()

    def test_get_random_fact(self):
        napi = Numbersapi()
        r, d = napi.get('/random/trivia')
        napi.verify(r.status_code, 200)
        napi.verify(d['text'])
        napi.verify(d['type'], 'trivia')
        napi.is_failed()

    def test_get_year_fact(self):
        napi = Numbersapi()
        r, d = napi.get('/1492/year')
        napi.verify(r.status_code, 200)
        napi.verify(d['text'])
        napi.verify(d['type'], 'year')
        napi.is_failed()

    def test_get_year_fact_year_bc(self):
        napi = Numbersapi()
        r, d = napi.get('/-1/year')
        napi.verify(r.status_code, 200)
        napi.verify(d['type'], 'year')
        napi.is_failed()

    def test_get_year_fact_year_negative(self):
        napi = Numbersapi()
        r, d = napi.get('/999999999/year')
        napi.verify(r.status_code, 200)
        napi.verify(d['found'], False)
        napi.is_failed()
