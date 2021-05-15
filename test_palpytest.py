import sys
from tmp import pal

def test_true():
    assert pal.palan("level") == True
def test_false():
    assert pal.palan("word") == False

