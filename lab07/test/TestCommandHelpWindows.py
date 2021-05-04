from CommandHelp import CommandHelp
import pytest

commandHelp = CommandHelp('windows')


class TestCommandHelpWindows:

    def test_command_doesnt_exist(self):
        result = commandHelp.info('piwo')
        assert result is None

    def test_command_with_upper_case_param(self):
        result = commandHelp.info('ping', '/T')
        assert result == 'ping /t: Specifies ping continue sending echo Request messages to the destination until interrupted. To interrupt and display statistics, press CTRL+ENTER. To interrupt and quit this command, press CTRL+C.'

    def test_command_with_lower_case_param(self):
        result = commandHelp.info('ping', '/a')
        assert result == 'ping /a: Specifies reverse name resolution be performed on the destination IP address. If this is successful, ping displays the corresponding host name.'

    def test_command_without_param(self):
        result = commandHelp.info('cmd')
        assert result is None

    def test_command_param_doesnt_exist(self):
        result = commandHelp.info('whoami', '/robs')
        assert result is None

    def test_command_with_upper_case(self):
        result = commandHelp.info('WHOAMI', '/user')
        assert result == 'whoami /user: Displays the current domain and user name and the security identifier (SID).'

    # pytest parametrize

    test_data_command_not_exists = [
        ('ping', '', None),
        ('ping', 'piwo', None),
        ('PING', 'piwo', None)
    ]

    @pytest.mark.parametrize('command,param,expected', test_data_command_not_exists)
    def test_data_if_command_exists(self, command, param, expected):
        result = commandHelp.info(command, param)
        assert result == expected

    test_data_command_with_param = [
        ('ping', '/t', 'ping /t: Specifies ping continue sending echo Request messages to the destination until interrupted. To interrupt and display statistics, press CTRL+ENTER. To interrupt and quit this command, press CTRL+C.'),
        ('ping', '/a', 'ping /a: Specifies reverse name resolution be performed on the destination IP address. If this is successful, ping displays the corresponding host name.')
    ]

    @pytest.mark.parametrize('command,param,expected', test_data_command_with_param)
    def test_data_command_with_param(self, command, param, expected):
        result = commandHelp.info(command, param)
        assert result == expected
