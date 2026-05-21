def run(items: list) -> bool:
    all_same = True
    item_to_comparate = items[0]
    for item in items[1:]:
        if item != item_to_comparate:
            all_same = False
            break
        else:
            all_same = True
    return all_same


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
