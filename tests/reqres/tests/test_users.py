from src.reqres.User import FullUser
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
