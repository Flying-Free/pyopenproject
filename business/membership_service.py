from abc import ABCMeta, abstractmethod


class MembershipService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_all(self): raise NotImplementedError

    @abstractmethod
    def find(self, membership): raise NotImplementedError

    @abstractmethod
    def update_membership(self, membership): raise NotImplementedError

    @abstractmethod
    def delete_membership(self, membership): raise NotImplementedError

    @abstractmethod
    def new_membership(self, membership): raise NotImplementedError

    @abstractmethod
    def membership_schema(self): raise NotImplementedError

    @abstractmethod
    def available_memberships(self): raise NotImplementedError

    @abstractmethod
    def new_membership_form(self, membership): raise NotImplementedError

    @abstractmethod
    def update_membership_form(self, membership): raise NotImplementedError
