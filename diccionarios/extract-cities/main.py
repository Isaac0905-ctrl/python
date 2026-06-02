def run(cinfo: str) -> dict:
    cinfo = cinfo.replace(';', ':').split(':')
    index = 0
    cities = {}
    while index < len(cinfo):
        city = cinfo[index]
        index += 1
        population = cinfo[index]
        index += 1
        cities[city] = int(population)
    return cities


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
