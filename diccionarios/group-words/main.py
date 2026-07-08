def run(words: list) -> dict:
    group_words = {}
    for item in words:
        letter_first = item[0]
        if letter_first not in group_words:
            values = []
            values.append(item)
            group_words[letter_first] = values
        else:
            values = group_words[letter_first]
            values.append(item)
            group_words[letter_first] = values
    return group_words


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
