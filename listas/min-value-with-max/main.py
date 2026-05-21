def run(values: list) -> int:
    values = [-value for value in values]
    min_value = max(values)
    return -min_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
