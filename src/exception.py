class MontantMinAtteint(Exception):
    def __init__(self, message):
        self.message = message


class MontantNegatif(Exception):
    def __init__(self, message):
        self.message = message
