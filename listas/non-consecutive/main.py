def run(values: list) -> int | None:
    if len(values) < 1:
        target = None
    else:
        num_to_comparate = values[0]
        for number in values:
            if number == num_to_comparate:
                num_to_comparate += 1
                target = None
            else:
                target = number
                break
    return target


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
