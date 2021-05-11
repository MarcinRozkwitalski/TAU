import pytest

def addition(a,b):
    return a + b

@pytest.mark.parametrize('a,b,result', [
    (1,2,3),
    ('raz',' dwa', 'raz dwa'),
    (13.37,21.37,34.74),
    ("dzien"," dobry","dzien dobry")])

def test_addition(a,b,result):
    assert addition(a,b) == result