def run(cinfo: str) -> dict:
    cities = {}
    for city, population in cinfo.items():
        cities[city] = population
    return cities


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
