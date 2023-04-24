import pytest

from task1 import delete_non_alphabet_and_spaces


def test_string_unchanged():
    assert delete_non_alphabet_and_spaces('hello world b a') == 'hello world b a'


def test_registry():
    assert delete_non_alphabet_and_spaces('HELLO WORLD B A') == 'hello world b a'


def test_punctuation():
    assert delete_non_alphabet_and_spaces('hello, world: b, a!') == 'hello world b a'


def test_non_latin():
    assert delete_non_alphabet_and_spaces('hello world b aцш!') == 'hello world b a'


def test_mixed():
    assert delete_non_alphabet_and_spaces('HELLO, world: b, a,цш!') == 'hello world b a'


if __name__ == '__main__':
    pytest.main("-vv")