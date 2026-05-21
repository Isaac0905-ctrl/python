def run(letters: str) -> list[str]:
    queue = []
    position = 0
    for letter in letters:
        if letter.isupper():
            queue.insert(position, letter)
            position +=1
        elif letter == ' ':
            queue = []
            position = 0
        elif letter.islower():
            queue.append(letter)
    return queue


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
