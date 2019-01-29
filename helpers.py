def print_output(f):
    def wrapper(*args, **kwargs):
        out = f(*args, **kwargs)
        print(out)
        return out
    return wrapper
