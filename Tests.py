import pytest
from main import *


class TestPytest:

    @classmethod
    def setup_class(cls):
        print('setup class')

    def setup(self):
        print('setup')

    @pytest.mark.parametrize('doc_number', [doc['number'] for doc in documents])
    def test_check_document_existance(self, doc_number):
        assert check_document_existance(doc_number) is True

    @pytest.mark.parametrize('user_doc_number, expected_result', [(doc['number'], doc['name']) for doc in documents])
    def test_get_doc_owner_name(self, user_doc_number, expected_result):
        assert get_doc_owner_name(user_doc_number) == expected_result

    def test_get_all_doc_owners_names(self):
        assert get_all_doc_owners_names() == {doc['name'] for doc in documents}

    @pytest.mark.parametrize('shelf_number', directories.keys())
    def test_add_new_shelf(self, shelf_number):
        assert add_new_shelf(shelf_number) == (shelf_number, False)

    @pytest.mark.parametrize('user_doc_number, expected_result', [('2207 876234', '1'),
                                                                  ('11-2', '1'),
                                                                  ('10006', '2')])
    def test_get_doc_shelf(self, user_doc_number, expected_result):
        assert get_doc_shelf(user_doc_number) == expected_result

    @pytest.mark.parametrize('user_doc_number, user_shelf_number, expected_result', [('10006', '1', '1')])
    def test_move_doc_to_shelf(self, user_doc_number, user_shelf_number, expected_result):
        assert move_doc_to_shelf(user_doc_number, user_shelf_number) == expected_result

    @pytest.mark.parametrize('new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, expected_result',
                             [('111', 'passport', 'Mr.Green', '15', '15')])
    def test_add_new_doc(self, new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, expected_result):
        assert add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number) == expected_result

    @pytest.mark.parametrize('user_doc_number', [doc['number'] for doc in documents])
    def test_delete_doc(self, user_doc_number):
        assert delete_doc(user_doc_number) == (user_doc_number, True)

    def teardown(self):
        print('teardown')

    @classmethod
    def teardown_class(cls):
        print('teardown class')
