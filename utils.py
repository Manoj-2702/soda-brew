class Array(list):
    def map(self, func):
        return Array(map(func, self))


class ArrayFactory:
    def __getitem__(self, items):
        if isinstance(items, tuple):
            return Array(items)
        if items == ...:
            return Array()
        return Array(items)


A = ArrayFactory()
