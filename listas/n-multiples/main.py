def run(x: int, n: int) -> list:
    multiples = [x * number for number in range(1, n + 1)]
    return multiples


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
