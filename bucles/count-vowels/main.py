def run(text):
    VOWELS = 'aeiouáéíóú'
    
    num_vowels = 0
    text = text.lower()
    for letra in text:
        if letra in VOWELS:
            num_vowels += 1
    return num_vowels


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
