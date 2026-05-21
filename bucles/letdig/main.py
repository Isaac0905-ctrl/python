def run(text: str) -> tuple[int, int]:
    num_digits = 0
    num_letters = 0
    text = text.lower()
    for char in text:
        if char.isdigit():
            num_digits +=1
        elif char.isalpha():
            num_letters +=1
    return num_letters, num_digits


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
