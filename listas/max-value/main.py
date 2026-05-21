def run(values: list) -> int:
    value_to_comparate = values[0]
    for value in values[0:]:
        if value >= value_to_comparate:
            value_to_comparate = value
            max_value =  value_to_comparate
        else:
            continue
    return max_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
