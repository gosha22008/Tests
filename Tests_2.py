import pytest
from Api_YD import *


class TestPytest1:

    @classmethod
    def setup_class(cls):
        print('setup class')

    def setup(self):
        print('setup')

    @pytest.mark.parametrize('expected_result', [201])
    def test_create_direct(self, expected_result):
        pap = YD()
        assert pap.create_direct() == expected_result

    @pytest.mark.parametrize('expected_result', [400, 401, 403, 404, 503])
    def test_create_direct_1(self, expected_result):
        pap = YD()
        assert pap.create_direct() != expected_result

    def teardown(self):
        print('teardown')

    @classmethod
    def teardown_class(cls):
        print('teardown class')