def run(limit: int) -> None:
    number = 5
    while number < limit:
        print(number)
        number +=5


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
