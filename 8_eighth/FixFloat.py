def fix(n):
    def decorator(function_to_decorate):
        def wrapper(*args, **kwargs):
            args = list(args)
            for i in range(len(args)):
                if type(args[i]) == float:
                    args[i] = round(args[i], n)
            for i in kwargs:
                if type(kwargs[i]) == float:
                    kwargs[i] = round(kwargs[i], n)
            
            args = tuple(args)
            result = function_to_decorate(*args, **kwargs)
            if type(result) == float:
                return round(result, n)
            else:
                return result
        return wrapper
    return decorator