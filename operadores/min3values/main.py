def run(value1: int | float, value2: int | float, value3: int | float) -> int | float:
    if value3 < value2 and value3 < value1:
        min_value = value3
    elif value2 < value3 and  value2 < value1:
        min_value = value2
    else:
        min_value = value1
    return min_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
