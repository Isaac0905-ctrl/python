def run(items: list) -> list:
    flatten_items = []
    for item in items:
        if isinstance(item, list):
            for value in item:
                flatten_items.append(value)
        else:
            flatten_items.append(item)
    return flatten_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
