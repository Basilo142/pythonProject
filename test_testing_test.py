import pytest
users = [{"name": "John", "age": 34},
         {"name": "James", "age": 9},
         {"name": "Aaron", "age": 56},
         {"name": "Alice", "age": 8},
         {"name": "Jen", "age": 17}]


@pytest.mark.parametrize('dict_users', users)
def test_age(dict_users):

    assert dict_users['age'] >= 18, dict_users['name']