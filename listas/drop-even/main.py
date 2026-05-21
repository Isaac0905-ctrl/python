def run(items: list) -> list:
    filtered = []
    for index, item in enumerate(items):
        if index % 2 == 1:
            filtered.append(item)
        else:
            continue
    return filtered


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
