from unittest import TestCase
import main
from unittest.mock import patch


class TestApp(TestCase):
    def test_user_action_string(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('exit',)
            main.logic()
            mocked_input.assert_called_with("Type 'add' or 'show' or 'exit': ")