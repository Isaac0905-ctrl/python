def run(fullname: str) -> str:
    SPACE = ' '
    index = 0
    lastname, name = fullname.upper().split(',')
    name = name.lstrip()
    name = name[0]
    initials = f'{name}.'
    initials += lastname[0] + '.'

    for letter in lastname:
        if letter == SPACE:
            initials += lastname[index + 1] + '.'
            break
        else:
            index += 1
    return initials


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
