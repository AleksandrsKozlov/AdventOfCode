import time

def run_with_measurment(function, print_result=False, use_nanoseconds=False, **kwargs):
    start_time = time.time_ns() if use_nanoseconds else time.time()
    result = function(**kwargs)
    end_time = time.time_ns() if use_nanoseconds else time.time()
    time_diff = end_time - start_time
    elapsed_time = time_diff if use_nanoseconds else time_diff * 1000

    if print_result:
        print(f"{function.__name__} result: {result}")
    units = "nanoseconds" if use_nanoseconds else "miliseconds"
    print(f"{function.__name__} process took: {elapsed_time} {units}")
    print()

    return result