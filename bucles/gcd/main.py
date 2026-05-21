def run(a: int, b: int) -> int:
    divisor = 1
    gcd_value = 1
    while divisor <= a and divisor <= b:
        if a % divisor == 0 and b % divisor == 0:
            gcd_value = divisor
        divisor += 1
    return gcd_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
