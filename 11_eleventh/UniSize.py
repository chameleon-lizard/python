class c():
    def __get__(self, obj, cl):
        if "__len__" in dir(obj):
            return len(obj)
        else:
            return int(obj)

def sizer(base):
    class new(base):
        size = c()
    return new