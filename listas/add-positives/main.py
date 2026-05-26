def run(numbers: list) -> int:
    positives_numbers = [num for num in numbers if num > 0]
    result = sum(positives_numbers)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
