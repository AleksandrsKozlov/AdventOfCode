import time

def run_with_measurment(function, print_result=False, **kwargs):
    start_time = time.time()
    result = function(**kwargs)
    end_time = time.time()
    elapsed_time_ms = (end_time - start_time) * 1000

    if print_result:
        print(f"{function.__name__} result: {result}")
    print(f"{function.__name__} process took: {elapsed_time_ms} milliseconds")
    print()

    return result