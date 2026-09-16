from utils.validators import is_valid_mac


def test_valid_mac():
    assert is_valid_mac("00:11:22:33:44:55") is True


def test_invalid_mac():
    assert is_valid_mac("invalid-mac") is False


def test_another_valid_mac():
    assert is_valid_mac("AA-BB-CC-DD-EE-FF") is True