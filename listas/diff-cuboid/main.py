def run(cuboid1: list, cuboid2: list) -> float:
    result_cuboid1 = 1
    result_cuboid2 = 1
    if len(cuboid1) and len(cuboid2) >= 1:
        for value_cuboid1, value_cuboid2 in zip(cuboid1, cuboid2):
            result_cuboid1 *= value_cuboid1
            result_cuboid2 *= value_cuboid2
        if result_cuboid1 > result_cuboid2:
            vol_diff = result_cuboid1 - result_cuboid2
        else:
            vol_diff = result_cuboid2 - result_cuboid1
    else:
        vol_diff = 0
    return vol_diff


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
