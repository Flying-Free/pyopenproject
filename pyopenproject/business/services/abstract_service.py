from abc import ABCMeta


class AbstractService:
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        self.connection = connection
