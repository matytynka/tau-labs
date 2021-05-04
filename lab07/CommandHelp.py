class CommandHelp:
    def __init__(self, driver):
        self.driver = driver
        if driver == 'windows':
            self.help = {
                'dir': {
                    '/n': 'Displays a long list format with file names on the far right of the screen.',
                    '/l': 'Displays unsorted directory names and file names, using lowercase.',
                    '/p': 'Displays one screen of the listing at a time. To see the next screen, press any key.'
                },
                'ping': {
                    '/t': 'Specifies ping continue sending echo Request messages to the destination until interrupted. To interrupt and display statistics, press CTRL+ENTER. To interrupt and quit this command, press CTRL+C.',
                    '/a': 'Specifies reverse name resolution be performed on the destination IP address. If this is successful, ping displays the corresponding host name.'
                },
                'whoami': {
                    '/user': 'Displays the current domain and user name and the security identifier (SID).',
                    '/groups': 'Displays the user groups to which the current user belongs.',
                    '/priv': 'Displays the security privileges of the current user.'
                },
                'where': {
                    '/f': 'Displays the results of the where command in quotation marks.',
                    '/t': 'Displays the file size and the last modified date and time of each matched file.'
                },
                'cmd': {
                    '/c': 'Carries out the command specified by string and then stops.',
                    '/k': 'Carries out the command specified by string and continues.',
                    '/d': 'Disables execution of AutoRun commands.'
                }
            }
        if driver == 'linux':
            self.help = {
                'pwd': {
                    '-L': 'use PWD from environment, even if it contains symlinks',
                    '-P': 'avoid all symlinks'
                },
                'ls': {
                    '-a': 'do not ignore entries starting with .',
                    '-A': 'do not list implied . and ..',
                    '-l': 'use a long listing format'
                },
                'cp': {
                    '-l': 'link files instead of copying',
                    '-u': 'copy only when the SOURCE file is newer than the destination file or when the destination file is missing'
                },
                'mv': {
                    '-f': 'do not prompt before overwriting',
                    '-i': 'prompt before overwrite',
                    '-n': 'do not overwrite an existing file'
                },
                'tar': {
                    '-A': 'append tar files to an archive',
                    '-c': 'create a new archive',
                    '-d': 'find differences between archive and file system'
                }
            }

    def info(self, command, param=''):
        if self.driver == 'windows':
            param = param.lower()
            command = command.lower()
        if command not in self.help:
            return None
        if param not in self.help[command]:
            return None
        return str(command + " " + param + ": " + self.help[command][param])
