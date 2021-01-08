from abc import ABCMeta, abstractmethod


class MembershipService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_all(self): raise NotImplementedError

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
    def available_memberships(self): raise NotImplementedError

    @abstractmethod
    def create_form(self, membership): raise NotImplementedError

    @abstractmethod
    def update_form(self, membership): raise NotImplementedError
