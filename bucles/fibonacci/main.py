def run(n: int) -> float:
    first_number = 0
    second_number = 1
    if n == 0:
        fibo = 0
    elif n == 1:
        fibo = 1
    else:
        for _ in range(0, n-1):
            fibo = first_number + second_number
            first_number = second_number
            second_number = fibo
    return fibo


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
