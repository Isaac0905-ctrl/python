def run(n: int) -> str:
    rest_the_divsion = []
    while n >= 0:
        quotient, remainder = divmod(n, 2)
        rest_the_divsion.append(str(remainder))
        n = quotient
    bin_repr = ''.join(rest_the_divsion[::-1])
    return bin_repr


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
