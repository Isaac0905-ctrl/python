def run(values: list) -> int:
    first_value = values[0]
    min_value = first_value
    for value in values[1:]:
        if value < first_value:
            min_value = value
    return min_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
