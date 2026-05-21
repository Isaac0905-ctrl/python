def run(matrix: list) -> int | None:
    sum_diagonal = 0
    for number in range(len(matrix)):
        if len(matrix) != len(matrix[0]):
            sum_diagonal = None
            break
        else:
            sum_diagonal += matrix[number][number]
    return sum_diagonal


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
