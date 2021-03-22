from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class MembershipService(AbstractService):
    """
    Class MembershipService,
    service for membership endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find_all(self, filters): raise NotImplementedError

    @abstractmethod
    def find(self, membership): raise NotImplementedError

    @abstractmethod
    def update(self, membership): raise NotImplementedError

    @abstractmethod
    def delete(self, membership): raise NotImplementedError

    @abstractmethod
    def create(self, membership): raise NotImplementedError

    @abstractmethod
    def membership_schema(self): raise NotImplementedError

    @abstractmethod
    def available_projects(self): raise NotImplementedError

    @abstractmethod
    def create_form(self, membership): raise NotImplementedError

    @abstractmethod
    def update_form(self, membership): raise NotImplementedError
