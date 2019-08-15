from tests.template import TestTemplate


class TestUsers(TestTemplate):
    def test_get_all_users(self):
        self.api.get('/api/users')
