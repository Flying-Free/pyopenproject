from business.services.grid_service import GridService
from business.services.impl.command.grid.create import Create
from business.services.impl.command.grid.find import Find
from business.services.impl.command.grid.find_all import FindAll
from business.services.impl.command.grid.update import Update


class GridServiceImpl(GridService):

    def find(self, grid):
        return Find(grid).execute()

    def find_all(self, offset, pageSize, filters, sortBy):
        return FindAll(offset, pageSize, filters, sortBy).execute()

    def create(self, grid):
        return Create(grid).execute()

    def update(self, grid):
        return Update(grid).execute()

    def create_form(self, grid):
        return Create(grid).execute()