def run(number: int) -> list:
    numbers = str(number)
    rev_digits = [int(num) for num in numbers]
    rev_digits = rev_digits[::-1]
    return rev_digits


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
