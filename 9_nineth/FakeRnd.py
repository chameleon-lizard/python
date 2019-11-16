call = -1

def randint(a, b):
    global call
    call += 1
    if not call % 2:
        return a
    else:
        return b

prevs = dict()
prevs['a'] = 0
prevs['b'] = 0
prevs['d'] = 0
prevs['current'] = 0 
def randrange(*args):
    if len(args) == 1:
        args = (0, args[0], 1)
    elif len(args) == 2:
        args = (args[0], args[1], 1)
    
    global prevs
    if args[0] == prevs['a'] and args[1] == prevs['b'] and args[2] == prevs['d']:
        prevs['current'] += prevs['d']
        if prevs['current'] >= prevs['b']:
            prevs['current'] = prevs['a'] + prevs['current'] - prevs['b']
            return prevs['current']
        return prevs['current']
    else:
        prevs['a'] = args[0]
        prevs['b'] = args[1]
        prevs['d'] = args[2]
        prevs['current'] = prevs['a']
        return prevs['current']