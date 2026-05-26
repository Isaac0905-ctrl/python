def run(numbers: list) -> int:
    numbers_to_sum = [-num for num in numbers]
    result = sum(numbers_to_sum)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
