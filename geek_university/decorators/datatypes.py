"""
    Forçando tipos de dados
"""



def forc_type(*types):
    def decorator(func):
        def convert(*args, **kwargs):
            new = []
            for (value, type) in zip(args, types):
                new.append(type(value))
            return func(*new, **kwargs)
        return convert
    return decorator


@forc_type(str, int)
def repete(msg, times):
    for time in range(times):
        print(msg)


repete('Oi', '6')