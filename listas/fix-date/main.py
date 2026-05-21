def run(input_date: str, base_year: int) -> str:
    input_date = input_date.split('/')
    day = input_date[1]
    month = input_date[0]
    year = base_year + int(input_date[2])
    output_date = f'{day}-{month}-{year}'
    return output_date


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
