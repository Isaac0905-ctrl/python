def run(numbers: str) -> str:
    if len(numbers) > 2:
        strip_numbers = ''
        items = numbers.split(',')
        del items[0]
        del items[-1]
        for item in items:
            strip_numbers += f'{item} '
        strip_numbers = strip_numbers.strip()
    else:
        strip_numbers = ''

    return strip_numbers


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
