def mul_with(x):
    def decorator(func):
        def new_func(*args, **kwargs):
            return x*func(*args, **kwargs)
        return new_func
    return decorator


@mul_with(4)
def mul4(a):
    return a

print(mul4(4))