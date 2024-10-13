import pytest

from lesson7.LessonException import RegistrationError
from lesson7.functions import registration

@pytest.mark.parametrize('username, password', [
    ('aaaa', 'b123vcnn'),
    ('ccccccccccccccc', 'cccccc23456ccccccccc')
])
def test_registration_true(username, password):
    assert registration(username, password) == True

@pytest.mark.parametrize('username, password', [
    ('aaa&a', 'b123vcnn'),
    ('cccccccccccccccc', 'cccccc23456cc!ccccccc')
])
def test_registration_false(username, password):
    with pytest.raises(RegistrationError, match="Введено некорректное значение username или password"):
        registration(username, password)

