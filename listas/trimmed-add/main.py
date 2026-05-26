def run(values: list) -> int:
    tsum = 0
    if len(values) < 1:
        tsum = 0
    else:
        min_value = min(values)
        max_value = max(values)
        for value in values:
            if value == min_value or value == max_value:
                continue
            else:
                tsum += value
    return tsum


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
