import pytest

from src.services.reqres.User import FullUser, UpdateUser
from tests.ReqresTemplate import ReqresTemplate


class TestUsers(ReqresTemplate):
    def test_get_all_users(self):
        r, d = self.api.get('/api/users')
        assert r.status_code == 200
        assert d['page'] == 1
        assert d['data']
        assert d['data'][0]['id'] == 1
        assert d['data'][0]['email'] == 'george.bluth@reqres.in'
        assert d['data'][0]['first_name'] == 'George'
        assert d['data'][0]['last_name'] == 'Bluth'

    def test_get_user(self):
        r, d = self.api.get('/api/users/1')
        assert r.status_code == 200
        assert d['data']['id'] == 1
        assert d['data']['email'] == 'george.bluth@reqres.in'
        assert d['data']['first_name'] == 'George'
        assert d['data']['last_name'] == 'Bluth'

    def test_get_unknown_user(self):
        r, d = self.api.get('/api/users/999999')
        assert r.status_code == 404

    def test_create_user(self):
        r, d = self.api.post('/api/users', FullUser().get_user_data())
        assert r.status_code == 200

    def test_update_user(self):
        r, d = self.api.put('/api/users/5', UpdateUser().get_user_data())
        assert r.status_code == 200

    @pytest.mark.xfail
    def test_delete_user(self):
        r, d = self.api.delete('/api/users/2')
        assert r.status_code == 204

    def test_login(self):
        r, d = self.api.post('/api/login', {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'})
        assert r.status_code == 200

    @pytest.mark.xfail
    def test_login_negative(self):
        r, d = self.api.post('/api/login', {'email': 'eve.holt@reqres.in'})
        assert r.status_code == 400

    def test_delay_response(self):
        r, d = self.api.get('/api/users?delay=3')
        assert r.status_code == 200
        assert d['data']
        assert d['page'] == 1