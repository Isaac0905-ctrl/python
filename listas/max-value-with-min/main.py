def run(values: list) -> int:
    max_value = [value for value in values if value > min(values)]
    return max_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
