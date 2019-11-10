def statcounter():
    stat = dict()
    function = yield stat

    while True:
        def wrapper(*args, function = function):
            if function in stat:
                stat[function] += 1
            else:
                stat[function] = 1
            return function(*args)
        function = yield wrapper