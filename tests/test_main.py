from unittest.mock import patch
from main import main


def test_main():
    with patch("builtins.input", return_value="4"):
        assert main() is None
