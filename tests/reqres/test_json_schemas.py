from src.services.reqres.reqres import Reqres


class TestReqresJsonSchemas:
    def test_check_users_schema(self):
        reqres = Reqres()
        _, d = reqres.get('/api/users')
        reqres.verify_json_schema(d, 'users.json')

        reqres.is_failed()
