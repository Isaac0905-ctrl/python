def run(start_code: int, end_code: int) -> None:
    SPACE = chr(32) * 3

    counter = 1
    for digit in range(start_code, end_code + 1):
        digit = str(digit)
        if len(digit) < 3 and counter == 5:
            print(f'0{digit}', chr(int(digit)), end=(SPACE))
            print()
            counter = 1
        elif len(digit) >= 3 and counter == 5:
            print(f'{digit}', chr(int(digit)), end=(SPACE))
            print()
            counter = 1
        elif len(digit) < 3:
            print(f'0{digit}', chr(int(digit)), end=(SPACE))
            counter+=1
        else:
            print(f'{digit}', chr(int(digit)), end=(SPACE))
            counter+=1


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
