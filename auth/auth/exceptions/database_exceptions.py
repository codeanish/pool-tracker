class UserNotFoundError(Exception):
    def __init__(self, message: str = "User not found"):
        """Exception raised when a user is not found in the database"""
        self.message = message
        super().__init__(self.message)
