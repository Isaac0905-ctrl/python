def run(text: str) -> bool:
    sotored_leterrs = []
    
    for letter in text.lower():
        if not letter.isalpha():
            continue
        elif letter not in sotored_leterrs:
            isogram = True
            sotored_leterrs.append(letter)
        else:
            isogram = False
            break
    return isogram


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
