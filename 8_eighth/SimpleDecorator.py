def nonify(func):
    def decorator(*arg, **kwarg):
        retvalue = func(*arg, **kwarg)
        if retvalue:
            return retvalue
        else:
            return None
    return decorator