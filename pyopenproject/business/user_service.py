from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class UserService(AbstractService):
    """
    Class UserService,
    service for user endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find_all(self, offset, page_size, filters, sort_by): raise NotImplementedError

    @abstractmethod
    def find(self, user): raise NotImplementedError

    @abstractmethod
    def lock(self, user): raise NotImplementedError

    @abstractmethod
    def unlock(self, user): raise NotImplementedError

    @abstractmethod
    def update(self, user): raise NotImplementedError

    @abstractmethod
    def delete(self, user): raise NotImplementedError

    @abstractmethod
    def create(self,
               login,
               email,
               first_name,
               last_name,
               admin,
               language,
               status,
               password): raise NotImplementedError

    @abstractmethod
    def invite(self, first_name, email): raise NotImplementedError
