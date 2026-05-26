def run(farm: list) -> str:
    WOLF = 'lobo'
    lenght = len(farm)
    index = 0
    if farm[-1] == WOLF:
        msg = 'Oye lobo no te quiero ver más por aquí'
    else:
        for animal in farm:
            if animal == WOLF:
                index += 1
                msg = f'Cuidado oveja {lenght-index}, el lobo te va a comer'
            else:
                index += 1
    return msg


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
