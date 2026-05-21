def run(key1: str, key2: str, key3: str) -> str:

    key1 = key1.upper()
    key2 = key2.upper()
    key3 = key3.upper()

    if ((key1 == 'CTRL' and key2 == 'ALT') or
        (key1 == 'ALT' and key2 == 'CTRL')) and key3 == 'T':
        return 'Open terminal'

    elif ((key1 == 'CTRL' and key2 == 'ALT') or
          (key1 == 'ALT' and key2 == 'CTRL')) and key3 == 'L':
        return 'Lock screen'

    elif ((key1 == 'CTRL' and key2 == 'ALT') or
          (key1 == 'ALT' and key2 == 'CTRL')) and key3 == 'D':
        return 'Show desktop'

    elif key1 == 'ALT' and key2 == 'F2' and key3 == '':
        return 'Run console'

    elif key1 == 'CTRL' and key2 == 'Q' and key3 == '':
        return 'Close window'

    elif ((key1 == 'CTRL' and key2 == 'ALT') or
          (key1 == 'ALT' and key2 == 'CTRL')) and key3 == 'DEL':
        return 'Log out'

    return 'Undefined'


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
