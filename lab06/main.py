import unittest

class Commands():
    def __init__(self, system_name):
        self.system_name = system_name

        self.linux_commands = {
            'ls': {
                'description': 'Used to change the current working directory.',
                '-l': 'Prints files in a long listing format.',
                '-la': 'Prints files in a long listing format and hidden files.'
            },
            'uptime': {
                'description': 'Show how long the system has been running + load.'
            },
            'hostname': {
                'description': 'Show system host name.',
                '-i': 'Display all local IP addresses of the host.'
            },
            'rm': {
                'description': 'Remove (delete) file',
                '-r': 'Remove the directory and its contents recursively.',
                '-f': 'Force removal of file without prompting for confirmation.'
            },
            'ps': {
                'description': 'Display your currently running processes.',
                '-ef': 'Display all the currently running processes on the system.'
            }
        }

        self.windows_commands = {
            'cd': {
                'description': 'Used to change the current working directory.',
                '..': 'Specifies that you want to change to the parent directory.'
            },
            'mkdir': {
                'description': 'Creates a directory or subdirectory.'
            },
            'shutdown': {
                'description': 'Shut downs system.',
                '/s': 'Shuts down system immediately.',
                '/r': 'Restarts system.'
            },
            'ping': {
                'description': 'Verifies IP-level connectivity to another TCP/IP computer by sending Internet Control '
                               'Message Protocol (ICMP) echo Request messages.',
                '-t': 'Pings the specified host until stopped. To stop - type Control-C.'
            },
            'ipconfig': {
                'description': 'Displays all current TCP/IP network configuration values and refreshes Dynamic Host '
                               'Configuration Protocol (DHCP) and Domain Name System (DNS) settings. ',
                '/all': 'Display the full TCP/IP configuration information for all network adapters.'
            }
        }

        if system_name == "Windows":
            self.commands = self.windows_commands
        elif system_name == "Linux":
            self.commands = self.linux_commands
        else:
            raise Exception("Wrong system name!")

    def does_command_exist(self, command):
        command = command.lower()
        if not isinstance(command, str):
            return None
        good = command.lower().split()
        if len(good) < 1:
            return None
        return good

    def show_command(self, command):
        command = command.lower()
        is_good = self.does_command_exist(command)
        if is_good is None:
            return None

        if is_good[0] in self.commands:
            command = self.commands[is_good[0]]
            if len(is_good) > 1:
                if is_good[1] in command:
                    return command[is_good[1]]
                else:
                    return command['description']
            else:
                return command['description']
        else:
            return None


class TestCommands(unittest.TestCase):
    def test_system_name_windows(self):
        system_name = "Windows"
        commands = Commands(system_name)
        assert commands.system_name == system_name

    def test_system_name_linux(self):
        system_name = "Linux"
        commands = Commands(system_name)
        assert commands.system_name == system_name

class TestLinux(unittest.TestCase):
    def test_linux_ls(self):
        command = Commands("Linux")
        result = command.show_command('ls')
        assert result == 'Used to change the current working directory.'

    def test_linux_ls_la(self):
        command = Commands("Linux")
        result = command.show_command('ls -la')
        assert result == 'Prints files in a long listing format and hidden files.'

    def test_linux_rm_f(self):
        command = Commands("Linux")
        result = command.show_command('rm -f')
        assert result == 'Force removal of file without prompting for confirmation.'

    def test_linux_hostname_i(self):
        command = Commands("Linux")
        result = command.show_command('hostname -i')
        assert result == 'Display all local IP addresses of the host.'

    def test_linux_uptime(self):
        command = Commands("Linux")
        result = command.show_command('uptime')
        assert result == 'Show how long the system has been running + load.'

class TestWindows(unittest.TestCase):
    def test_windows_cd(self):
        command = Commands("Windows")
        result = command.show_command('cd')
        assert result == 'Used to change the current working directory.'

    def test_windows_mkdir(self):
        command = Commands("Windows")
        result = command.show_command('mkdir')
        assert result == 'Creates a directory or subdirectory.'

    def test_windows_shutdown_s(self):
        command = Commands("Windows")
        result = command.show_command('shutdown /s')
        assert result == 'Shuts down system immediately.'

    def test_windows_ping_t(self):
        command = Commands("Windows")
        result = command.show_command('ping -t')
        assert result == 'Pings the specified host until stopped. To stop - type Control-C.'

    def test_windows_ipconfig_all(self):
        command = Commands("Windows")
        result = command.show_command('ipconfig /all')
        assert result == 'Display the full TCP/IP configuration information for all network adapters.'


if __name__ == '__main__':
    unittest.main()