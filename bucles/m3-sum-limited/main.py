def run(limit: int) -> None:
    result = 0
    value_to_sum1 = 0
    value_to_sum2 = 0
    for number in range(0, limit, 3):
        if result >= limit:
            break
        else:
            value_to_sum1 = number
            result = value_to_sum1 + value_to_sum2
            value_to_sum2 = result
            print(number, end=' ')


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
