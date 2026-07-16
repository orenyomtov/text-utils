from text_utils import word_count, dedupe_lines, slugify


def test_word_count():
    assert word_count("a b c") == 3


def test_dedupe_lines():
    assert dedupe_lines("x\nx\ny") == "x\ny"


def test_slugify():
    assert slugify("Hello World") == "hello-world"
