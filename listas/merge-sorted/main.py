def run(values1: list, values2: list) -> list:
    merged = []
    index_values1 = 0
    index_values2 = 0
    while index_values1 < len(values1) and index_values2 < len(values2):
        if (
            values1[index_values1] <= values2[index_values2]
            and values1[index_values1] not in merged
        ):
            merged.append(values1[index_values1])
            index_values1 += 1
        elif (
            values2[index_values2] <= values2[index_values2]
            and values2[index_values2] not in merged
        ):
            merged.append(values2[index_values2])
            index_values1 += 1
        else:
            index_values1 += 1
            index_values2 += 1
            continue
    merged += values1[index_values1:]
    merged += values2[index_values2:]

    return merged


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
