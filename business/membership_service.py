from abc import ABCMeta, abstractmethod


class MembershipService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_all(self): raise NotImplementedError

    @abstractmethod
    def find(self, membership): raise NotImplementedError

    # TODO: Review what params we need to create a new membership
    @abstractmethod
    def new_membership(self): raise NotImplementedError
