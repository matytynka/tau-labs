from CommandHelp import CommandHelp
import pytest

commandHelp = CommandHelp('linux')


class TestCommandHelpLinux:

    def test_command_doesnt_exist(self):
        result = commandHelp.info('piwo')
        assert result is None

    def test_command_with_bad_case_param(self):
        result = commandHelp.info('mv', '-F')
        assert result is None

    def test_command_with_good_case_param(self):
        result = commandHelp.info('cp', '-l')
        assert result == 'cp -l: link files instead of copying'

    def test_command_without_param(self):
        result = commandHelp.info('pwd')
        assert result is None

    def test_command_param_doesnt_exist(self):
        result = commandHelp.info('tar', '/robs')
        assert result is None

    def test_command_with_upper_case(self):
        result = commandHelp.info('MV', '-f')
        assert result is None

    # pytest parametrize

    test_data_command_not_exists = [
        ('pwd', None, None),
        ('pwd', 'piwo', None),
        ('PWD', None, None),
        ('PWD', 'piwo', None)
    ]

    @pytest.mark.parametrize('command,param,expected', test_data_command_not_exists)
    def test_data_if_command_exists(self, command, param, expected):
        result = commandHelp.info(command, param)
        assert result == expected

    test_data_command_with_param = [
        ('pwd', '-L', 'pwd -L: use PWD from environment, even if it contains symlinks'),
        ('pwd', '-P', 'pwd -P: avoid all symlinks')
    ]

    @pytest.mark.parametrize('command,param,expected', test_data_command_with_param)
    def test_data_command_with_param(self, command, param, expected):
        result = commandHelp.info(command, param)
        assert result == expected
