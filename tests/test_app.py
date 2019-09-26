import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/..')
print(sys.path)
from app.utils import make_message


class TestApp(object):

    @pytest.mark.parametrize(('name', 'expected'), {
        ('Ishizu', 'Hello Ishizu!'),
        ('Yuya', 'Hello Yuya!'),
    })
    def test_app(self, name, expected):
        print(sys.path)
        actual = make_message(name)

        assert actual == expecte
