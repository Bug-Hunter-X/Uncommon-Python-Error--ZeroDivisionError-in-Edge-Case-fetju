def function_with_uncommon_error(a, b):
    if a == 0 or b == 0:
        return 0 # Handle division by zero
    else:
        return a / b