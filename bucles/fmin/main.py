def run(x1: int, x2: int) -> tuple:
    result = x1**2 - (6 * x1) + 3
    xmin = result
    fmin = x1
    for number in range(x1 + 1, x2 + 1):
        result = number**2 - (6 * number) + 3
        if result < xmin:
            xmin = result
            fmin = number
    return fmin, xmin

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
