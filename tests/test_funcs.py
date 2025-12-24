from src.funcs import factorial, factorial_recursive, fib, fibo_recursive


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(7) == 5040
    assert factorial(32) == 263130836933693530167218012160000000


def test_factorial_recursive_same_as_iterative():
    for n in range(0, 10):
        assert factorial_recursive(n) == factorial(n)
    assert factorial(15) == 1307674368000
    assert factorial(17) == 355687428096000
    assert factorial(32) == 263130836933693530167218012160000000


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(5) == 5
    assert fib(10) == 55
    assert fib(17) == 1597


def test_fibo_recursive_same_as_iterative():
    for n in range(0, 30):
        assert fibo_recursive(n) == fib(n)
