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
 
@fix(4)
def aver(*args, sign=1):
    return sum(args)*sign

print(aver(2.45675901, 3.22656321, 3.432654345, 4.075463224, sign=-1))