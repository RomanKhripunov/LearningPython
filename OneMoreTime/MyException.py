class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x < 1:
            raise NonPositiveError()
        super(PositiveList, self).append(x)
