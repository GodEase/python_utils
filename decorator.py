import time
import functools


def perf(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        st = time.time()
        ret = func(*args, **kwargs)
        args_str = ', '.join([f'{i}' for i in args] +
                             [f'{i}={kwargs[i]}' for i in kwargs.keys()])
        print(f"Run {func.__name__}({args_str}), "
              f"cost {time.time() - st:.3f}s.")
        return ret

    return wrapper
