def run(values: list, power: int) -> int:
    if len(values) > power:
        result = values[power]**power
    else:
        result = -1
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
