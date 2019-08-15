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
