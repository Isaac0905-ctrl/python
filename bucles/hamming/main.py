def run(text1: str, text2: str) -> int:
    dhamming = 0
    if len(text1) == len (text2):
        for letter_up, letter_down in zip(text1, text2):
            if letter_up == letter_down:
                dhamming += 0
            else:
                dhamming += 1
    else:
        dhamming = -1
    return dhamming


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
