def run(numbers: list) -> int:
    rmult = 0
    if len(numbers) == 1:
        rmult = numbers[0]
    elif len(numbers) < 1:
        rmult = 1
    else:
        num_to_multiplicate = numbers[0]
        for number in numbers[1:]:
            rmult = num_to_multiplicate * number
            num_to_multiplicate = rmult
    return rmult


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
