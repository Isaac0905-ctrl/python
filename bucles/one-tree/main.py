def run():
    number_to_multp = '1'
    multiplications = 1
    while multiplications < 10:
        result = int(number_to_multp) * int(number_to_multp)
        print(result)
        number_to_multp = str(number_to_multp) 
        number_to_multp = number_to_multp + '1'
        multiplications+=1
        


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
