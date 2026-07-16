def run(items: dict) -> dict:
    citems = {key: ([] if len(value) > 1 else value) for key, value in items.items()}
    return citems


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
