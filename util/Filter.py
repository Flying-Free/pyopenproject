class Filter:

    def __init__(self, name, operator, values):
        """ Constructor for class Filter

        :param name: The name of the filter
        :param operator: The operator
        :param values: The Filter values
        """
        self.name = name
        self.operator = operator
        self.values = values
