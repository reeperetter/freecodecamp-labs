def square_root_bisection(number: int | float, tolerance: int | float = 0.5, iterations: int = 1):
    if number < 0:
        raise ValueError(
            'Square root of negative number is not defined in real numbers')
    elif number in [0, 1]:
        print(f'The square root of {number} is {number}')
        return number

    low = 0.0
    high = max(1.0, float(number))

    for _ in range(iterations):
        mid = (low + high) / 2.0
        square_mid = mid ** 2

        if abs(square_mid - number) < tolerance:
            print(f'The square root of {number} is approximately {mid}')
            return mid

        if square_mid > number:
            high = mid
        else:
            low = mid

    print(f'Failed to converge within {iterations} iterations')
    return None


print(square_root_bisection(0.001, 1e-7, 50))
