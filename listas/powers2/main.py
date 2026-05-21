def run(n: int) -> list:
    powers2 = []
    for number in range(0, n+1):
        result = 2**number
        powers2.append(result)
    return powers2


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
