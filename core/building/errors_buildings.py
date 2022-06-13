class WrongInputType(Exception):
    def __init__(self):
        self.message = "All arguments must be numbers"
