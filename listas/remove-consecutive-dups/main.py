def run(items: list) -> list:
    result = []
    item_to_comparate = items[0]
    result.append(item_to_comparate)
    for item in items[1:]:
        if item != item_to_comparate:
            result.append(item)
            item_to_comparate = item
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
