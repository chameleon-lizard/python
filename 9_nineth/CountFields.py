def fcounter(C, *args, **kwargs):
    cm = []
    for i in dir(C):
        if not i.startswith('_'):
            if callable(getattr(C, i)):
                cm.append(i)
    cm.sort()

    cf = []
    for i in dir(C):
        if not i.startswith('_'):
            if not callable(getattr(C, i)):
                cf.append(i)
    cf.sort()

    E = C(*args, **kwargs)

    em = []
    for i in dir(E):
        if not i.startswith('_'):
            if callable(getattr(E, i)):
                if not i in cm:
                    em.append(i)
    em.sort()

    ef = []
    for i in dir(E):
        if not i.startswith('_'):
            if not callable(getattr(E, i)):
                if not i in cf:
                    ef.append(i)
    ef.sort()

    return (cm, cf, em, ef)