def run(fullname: str) -> str:
    fullname = fullname.upper().replace(',','')
    initials = fullname[0]+'.'
    index = 0
    SPACE = ' '
    for letter in fullname:
        if letter == SPACE:
            initials += fullname[index + 1]+'.'
            index += 1
        else:
            index += 1
    return initials


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
