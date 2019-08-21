from core.helpers.DataGeneration import DataGeneration


class User:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.email = None
        self.job = None

    def set_first_name(self, value):
        self.first_name = value

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, value):
        self.last_name = value

    def get_last_name(self):
        return self.last_name

    def set_email(self, value):
        self.email = value

    def get_email(self):
        return self.email

    def set_job(self, value):
        self.job = value

    def get_job(self):
        return self.job

    def get_user_data(self):
        return {
            'first_name': self.get_first_name(),
            'last_name': self.get_last_name(),
            'email': self.get_email(),
            'job': self.get_job()
        }


class FullUser(User):
    def __init__(self):
        super().__init__()
        self.set_first_name(DataGeneration.random_string())
        self.set_last_name(DataGeneration.random_string())
        self.set_email('{}@autotest.com'.format(DataGeneration.random_string()))
        self.set_job(DataGeneration.random_string())
