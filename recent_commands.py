class RecentCommands:
    def __init__(self):
        self.recent_commands = []

    def add_command(self, command):
        self.recent_commands.append(command)

    def get_recent_commands(self):
        return self.recent_commands

    def clear_commands(self):
        self.recent_commands = []
