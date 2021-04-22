from CommandHelp import CommandHelp

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
