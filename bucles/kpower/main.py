def run(n: int) -> tuple:
    left_side, right_side = 0, 0
    for number in range(1, n+1):
        left_side += number
        right_side += number**3
    left_side = left_side**2

    return left_side, right_side


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
