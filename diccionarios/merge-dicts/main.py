def run(d1: dict, d2: dict) -> dict:
    merged = {}
    for data_1, data_2 in zip(d1.items(), d2.items()):
        if isinstance(data_1, tuple) and isinstance(data_2, tuple):
            key, value = data_1
            merged[key] = value

            key, value = data_2
            merged[key] = value
    return merged


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
