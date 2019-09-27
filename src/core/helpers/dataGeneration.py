import random
import string


class DataGeneration:
    @staticmethod
    def random_string(letters=10):
        return ''.join(random.sample(string.ascii_lowercase + string.digits, letters))

    @staticmethod
    def random_int(m, n):
        return random.randint(m, n)
