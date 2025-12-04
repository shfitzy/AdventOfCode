import functools
import statistics
import time

def timer(func, name, n, *args, **kwargs):
    """Decorator that times the execution of a function.
    
    Can be used as a decorator or called directly with function arguments.
    If arguments are provided, the function is called immediately and timed.
    If no arguments are provided, returns a wrapped function that can be called later.
    """
    @functools.wraps(func)
    def wrapper(*wrapper_args, **wrapper_kwargs):
        # Use provided args/kwargs if available, otherwise use wrapper args/kwargs
        final_args = args if args else wrapper_args
        final_kwargs = kwargs if kwargs else wrapper_kwargs
        
        times = []

        for i in range(n):
            start_time = time.time()
            result = func(*final_args, **final_kwargs)
            end_time = time.time()

            times.append(end_time - start_time)

        print(f"{name}: {result}\n     Avg: {(statistics.mean(times)*1000):.2f}ms\n  Median: {statistics.median(times)*1000:.2f}ms\n     Min: {min(times)*1000:.2f}ms\n     Max: {max(times)*1000:.2f}ms\n")
        return result
    
    # If arguments were provided, call the function immediately
    if args or kwargs:
        return wrapper()
    
    # Otherwise, return the wrapper function for later use
    return wrapper
