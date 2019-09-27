import pytest

from src.services.reqres.reqres import Reqres
from src.services.reqres.user import FullUser, UpdateUser


class TestUsers:
    def test_get_all_users(self):
        reqres = Reqres()
        r, d = reqres.get('/api/users')
        reqres.verify(r.status_code == 200)
        reqres.verify(d['page'] == 1)
        reqres.verify(d['data'])
        reqres.verify(d['data'][0]['id'] == 1)
        reqres.verify(d['data'][0]['email'] == 'george.bluth@reqres.in')
        reqres.verify(d['data'][0]['first_name'] == 'George')
        reqres.verify(d['data'][0]['last_name'] == 'Bluth')
        reqres.is_failed()

    def test_get_user(self):
        reqres = Reqres()
        r, d = reqres.get('/api/users/1')
        reqres.verify(r.status_code == 200)
        reqres.verify(d['data']['id'] == 1)
        reqres.verify(d['data']['email'] == 'george.bluth@reqres.in')
        reqres.verify(d['data']['first_name'] == 'George')
        reqres.verify(d['data']['last_name'] == 'Bluth')
        reqres.is_failed()

    def test_get_unknown_user(self):
        reqres = Reqres()
        r, _ = reqres.get('/api/users/999999')
        reqres.verify(r.status_code == 404)
        reqres.is_failed()

    def test_create_user(self):
        reqres = Reqres()
        r, _ = reqres.post('/api/users', FullUser().get_user_data())
        reqres.verify(r.status_code == 200)
        reqres.is_failed()

    def test_update_user(self):
        reqres = Reqres()
        r, _ = reqres.put('/api/users/5', UpdateUser().get_user_data())
        reqres.verify(r.status_code == 200)
        reqres.is_failed()

    @pytest.mark.xfail
    def test_delete_user(self):
        reqres = Reqres()
        r, _ = reqres.delete('/api/users/2')
        reqres.verify(r.status_code == 204)
        reqres.is_failed()

    def test_login(self):
        reqres = Reqres()
        r, _ = reqres.post('/api/login', {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'})
        reqres.verify(r.status_code == 200)
        reqres.is_failed()

    @pytest.mark.xfail
    def test_login_negative(self):
        reqres = Reqres()
        r, _ = reqres.post('/api/login', {'email': 'eve.holt@reqres.in'})
        reqres.verify(r.status_code == 400)
        reqres.is_failed()

    def test_delay_response(self):
        reqres = Reqres()
        r, d = reqres.get('/api/users?delay=3')
        reqres.verify(r.status_code == 200)
        reqres.verify(d['data'])
        reqres.verify(d['page'] == 1)
        reqres.is_failed()
