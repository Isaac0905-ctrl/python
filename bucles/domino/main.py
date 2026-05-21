def run():
    for token in range(0, 7):
        for token_value in range(token, 7):
            print(f'{token}|{token_value}', end=(' '))
        print()


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
