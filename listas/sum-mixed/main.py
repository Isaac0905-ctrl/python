def run(items: list) -> int:
    sum_items = 0
    if len(items) < 2:
        sum_items = items[0]
    else:
        for item in items:
            if isinstance(item, str):
                sum_items += int(item)
            else:
                sum_items += item
    return sum_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
