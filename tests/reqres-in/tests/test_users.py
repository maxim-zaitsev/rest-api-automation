from tests.ReqresTemplate import ReqresTemplate


class TestUsers(ReqresTemplate):
    def test_get_all_users(self):
        self.api.get('/api/users')
