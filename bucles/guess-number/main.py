def run(target_number: int) -> None:
    attemps = 1
    while True:
        number = int(input('Introduzca número: '))
        if  number > target_number:
            print('Menor')
            attemps+=1
        elif number < target_number:
            print('Mayor')
            attemps+=1
        else:
            print(f'Enhorabuena has encontrado el número en {attemps} intentos')
            break


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
