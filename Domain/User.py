class User:
    def __init__(self, user_data):
        self.username = user_data[0]
        self.password = user_data[1]
        self.name = user_data[2]
        self.admin = user_data[3]
        self.hasPermissions = []

    def HasPermission(self, permission):
        return permission in self.hasPermissions
