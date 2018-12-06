def bad_fibonacci(n):
    '''Return the nth Fibonacci number'''
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)