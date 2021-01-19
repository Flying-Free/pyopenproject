from business.services.grid_service import GridService
from business.services.impl.command.grid.create import Create
from business.services.impl.command.grid.find import Find
from business.services.impl.command.grid.find_all import FindAll
from business.services.impl.command.grid.update import Update


class GridServiceImpl(GridService):
    def __init__(self, connection):
        super().__init__(connection)

    def find(self, grid):
        return Find(self.connection, grid).execute()

    def find_all(self, offset, page_size, filters, sort_by):
        return FindAll(self.connection, offset, page_size, filters, sort_by).execute()

    def create(self, grid):
        return Create(self.connection, grid).execute()

    def update(self, grid):
        return Update(self.connection, grid).execute()

    def create_form(self, grid):
        return Create(self.connection, grid).execute()
