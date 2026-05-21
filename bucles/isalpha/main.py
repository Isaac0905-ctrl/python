def run(text: str) -> bool:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    for char in text:
        if char in ALPHABET:
            isalpha = True
        else:
            isalpha = False
            break
    return isalpha


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
