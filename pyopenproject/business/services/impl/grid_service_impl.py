from pyopenproject.business.services.grid_service import GridService
from pyopenproject.business.services.impl.command import Create
from pyopenproject.business.services.impl.command import CreateForm
from pyopenproject.business.services.impl.command import Find
from pyopenproject.business.services.impl.command import Update
from pyopenproject.business.services.impl.command import UpdateForm
from pyopenproject.business.services.impl.command.grid.find_all import FindAll


class GridServiceImpl(GridService):
    def __init__(self, connection):
        super().__init__(connection)

    def find(self, grid):
        return Find(self.connection, grid).execute()

    def find_all(self, offset=None, page_size=None, filters=None, sort_by=None):
        return list(FindAll(self.connection, offset, page_size, filters, sort_by).execute())

    def create(self, grid):
        return Create(self.connection, grid).execute()

    def update(self, grid):
        return Update(self.connection, grid).execute()

    def create_form(self):
        return CreateForm(self.connection).execute()

    def update_form(self, grid, grid_form):
        return UpdateForm(self.connection, grid, grid_form).execute()
