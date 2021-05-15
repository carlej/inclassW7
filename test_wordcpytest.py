import pytest
from tmp import wordc

def test_wordcg():
    assert wordc.wordcount("this is a test") == 4
def test_wordcb():
    assert wordc.wordcount("this is a bad test") == 4
