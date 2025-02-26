import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970



def speed_calc_decorator(function):
    def wrapper_function():
        function()
        run_time = time.time() - current_time
        return run_time

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


print(f"fast_function run speed: {fast_function()}")
print(f"slow_function run speed: {slow_function()}")