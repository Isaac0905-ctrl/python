def run(target_x: int, target_y: int) -> int:
    movements = 1
    if target_x != target_y and target_x % 3 != 0:
        movements = -1
    return movements


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
