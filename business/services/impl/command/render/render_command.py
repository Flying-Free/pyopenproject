from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class RenderCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/render"

    @abstractmethod
    def execute(self): raise NotImplementedError
