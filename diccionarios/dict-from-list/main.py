def run(items: list) -> dict:
    unpack_items = {}
    for item in items:
        key = item[0]
        unpack_items[key] = item[1:]
    return unpack_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
