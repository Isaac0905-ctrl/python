def run(pdata: dict) -> dict:
    population_word = sum(pdata.values())
    avg_data = {}
    for city, population in pdata.items():
        avg_population = population / population_word
        avg_population = round((avg_population * 100), 3)
        avg_data[city] = avg_population
    return avg_data


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
