from max_seq import max_seq_len

def test_empty_string():
    assert max_seq_len("") == 0

def test_one_char():
    assert max_seq_len("b") == 1

def test_all_single():
    assert max_seq_len("abcdef") == 1

def test_generac_case():
    assert max_seq_len("adddcaa") == 3

def test_max_in_the_end():
    assert max_seq_len("abcdeeeee") == 5

def test_max_in_the_beginning():
    assert max_seq_len("eeeeeabcd") == 5

def test_equal_series():
    assert max_seq_len("eeeeeabcdeeeee") == 5