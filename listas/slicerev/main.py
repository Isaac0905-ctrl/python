def run(items: list[int]) -> list[int]:
    if len(items) >= 1:
        start = 0
        end = len(items)
        half = len(items) // 2
        step = items[half]
        result = items[start:end:step]
        result = result[::-1]
    else:
        result = []
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
