import os
import unittest


def extend_suite(cases):
    for case in cases:
        suite.addTest(case)


suite = unittest.TestSuite()

if int(os.getenv('reqres', '1')) == 1:
    from tests.reqres.tests.test_users import TestUsers

    extend_suite([TestUsers])


def run():
    unittest.TextTestRunner(verbosity=2).run(suite)