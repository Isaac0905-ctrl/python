def run(items: dict) -> dict:
    fitems = {}
    for key, value in items.items():
        clean_key = key.replace(' ','')
        fitems[clean_key] = value

    return fitems


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
