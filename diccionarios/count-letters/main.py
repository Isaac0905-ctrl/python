def run(text: str) -> dict:
    counter = {}
    for letter in text:
        if letter not in counter:
            letter_counter = 1
            counter[letter] = letter_counter
        else:
            counter[letter] += 1
    return counter


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
