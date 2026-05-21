def run(input_date: str, base_year: int) -> str:
    input_date = input_date.split('/')
    day = int(input_date[1])
    month = int(input_date[0])
    year = base_year + int(input_date[2])
    if day < 10:
        output_date = f'0{day}-{month}-{year}'
    elif month < 10:
        output_date = f'{day}-0{month}-{year}'
    elif year < 1000:
        output_date = f'{day}-{month}-0{year}'
    else:
        output_date = f'{day}-{month}-{year}'
    return output_date


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
