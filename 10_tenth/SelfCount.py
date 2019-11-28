class WeAre:
    _count = 0

    def __init__(self):
        WeAre._count += 1

    @property
    def count(self):
        return WeAre._count
    
    @count.setter
    def count(self, value):
        pass

    @count.deleter
    def count(self):
        pass
    
    def __del__(self):
        WeAre._count -= 1